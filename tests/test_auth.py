"""The device flow and refreshing tokens, against the sign-in's answers as RFC 8628 and OAuth write them."""

import json

import httpx
import pytest

from blupinta import BlupintaError, TokenKeeper, Tokens, refresh_tokens, start_device_sign_in


def sign_in(answers):
    """A sign-in that answers each request with the next of ``answers``, keeping what it was sent"""
    sent = []

    def handle(request: httpx.Request) -> httpx.Response:
        sent.append((request.url.path, dict(httpx.QueryParams(request.content.decode()))))
        status, body = answers.pop(0)
        return httpx.Response(status, content=json.dumps(body))

    return httpx.Client(transport=httpx.MockTransport(handle)), sent


def test_the_device_flow_waits_for_the_person_then_gives_the_tokens():
    http, sent = sign_in(
        [
            (200, {"device_code": "dc", "user_code": "BCDF-GHJK", "verification_uri": "https://a/device", "interval": 5}),
            (400, {"error": "authorization_pending"}),
            (400, {"error": "slow_down"}),
            (200, {"access_token": "at", "refresh_token": "rt", "expires_in": 3600, "scope": "openid", "id_token": "x"}),
        ]
    )
    started = start_device_sign_in("openid offline_access", http=http, auth_origin="https://a")
    assert started.user_code == "BCDF-GHJK"
    waits = []
    tokens = started.tokens(sleep=waits.append)
    assert tokens.access_token == "at" and tokens.refresh_token == "rt" and tokens.id_token == "x"
    # it slowed down when asked to
    assert waits == [5, 5, 10]
    assert sent[0] == ("/oidc/device/auth", {"client_id": "device", "scope": "openid offline_access", "resource": "https://api.blupinta.app/v1"})
    assert sent[1][1]["grant_type"] == "urn:ietf:params:oauth:grant-type:device_code"


def test_a_refused_device_is_an_error():
    http, _ = sign_in([(200, {"device_code": "dc", "user_code": "C", "interval": 1}), (400, {"error": "access_denied"})])
    with pytest.raises(BlupintaError) as refused:
        start_device_sign_in("openid", http=http).tokens(sleep=lambda _: None)
    assert "access_denied" in refused.value.problems[0]


def test_the_keeper_refreshes_before_the_token_expires_and_keeps_the_new_ones():
    http, sent = sign_in([(200, {"access_token": "fresh", "expires_in": 3600})])
    kept = []
    keeper = TokenKeeper(
        Tokens("old", "rt", expires_at=0, scope=""), client_id="cli", on_tokens=kept.append, http=http
    )
    assert keeper() == "fresh"
    assert keeper() == "fresh"
    assert len(sent) == 1 and sent[0][1]["refresh_token"] == "rt"
    # no refresh token came back: the old one goes on
    assert kept[0].refresh_token == "rt"


def test_a_refused_refresh_is_an_error():
    http, _ = sign_in([(400, {"error": "invalid_grant"})])
    with pytest.raises(BlupintaError):
        refresh_tokens("rt", client_id="cli", http=http)
