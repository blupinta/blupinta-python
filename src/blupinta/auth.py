"""Signing a person in at auth.blupinta.app (OAuth 2.1, OpenID Connect) to get the tokens ``/v1`` takes: the device
flow for a script or a screen without a keyboard (the person types a code on their phone), and refreshing a token
before it expires. Only requests to the sign-in's own endpoints: no secret is ever held."""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass
from typing import Any, Callable

import httpx

from .errors import BlupintaError

AUTH_ORIGIN = "https://auth.blupinta.app"
#: The resource ``/v1``'s tokens are for (RFC 8707)
API_RESOURCE = "https://api.blupinta.app/v1"
#: Blupinta's own client for a device that connects without registering: the person names it at consent
DEVICE_CLIENT_ID = "device"
DEVICE_GRANT = "urn:ietf:params:oauth:grant-type:device_code"


@dataclass(frozen=True)
class Tokens:
    """What the sign-in gives the app."""

    access_token: str
    #: when the app asked ``offline_access``: how it gets the next access token without the person
    refresh_token: str | None
    #: when the access token stops working, in seconds since 1970
    expires_at: float
    scope: str
    #: who signed in, as OpenID Connect's ID token says it, when ``openid`` was asked
    id_token: str | None = None


def _tokens_of(answer: dict[str, Any]) -> Tokens:
    if not isinstance(answer.get("access_token"), str):
        raise BlupintaError(500, "server_error", ["no access token"])
    return Tokens(
        access_token=answer["access_token"],
        refresh_token=answer.get("refresh_token"),
        expires_at=time.time() + float(answer.get("expires_in", 0)),
        scope=answer.get("scope", ""),
        id_token=answer.get("id_token"),
    )


def _refusal(status: int, answer: dict[str, Any]) -> BlupintaError:
    reason = ": ".join(str(part) for part in (answer.get("error"), answer.get("error_description")) if part)
    return BlupintaError(status, "unauthenticated" if status == 401 else "forbidden", [reason])


def _post(http: httpx.Client, url: str, fields: dict[str, str]) -> tuple[int, dict[str, Any]]:
    try:
        response = http.post(url, data=fields, headers={"accept": "application/json"})
    except httpx.HTTPError as e:
        raise BlupintaError(0, "network", [str(e)]) from e
    try:
        answer = response.json()
    except ValueError:
        answer = {}
    return response.status_code, answer if isinstance(answer, dict) else {}


class DeviceSignIn:
    """A device being connected: what to show the person, and how to wait for them."""

    def __init__(self, http: httpx.Client, token_url: str, client_id: str, answer: dict[str, Any]) -> None:
        self._http = http
        self._token_url = token_url
        self._client_id = client_id
        self._device_code: str = answer["device_code"]
        self._interval = float(answer.get("interval", 5))
        #: the code the person types (``BCDF-GHJK``)
        self.user_code: str = answer["user_code"]
        #: where they type it
        self.verification_uri: str = answer.get("verification_uri", "")
        #: the same, the code already in it: for a QR code
        self.verification_uri_complete: str = answer.get("verification_uri_complete", self.verification_uri)
        self.expires_at = time.time() + float(answer.get("expires_in", 600))

    def tokens(self, sleep: Callable[[float], None] = time.sleep) -> Tokens:
        """Waits until the person allows the device (its tokens), refuses, or the code expires."""
        while time.time() < self.expires_at:
            sleep(self._interval)
            status, answer = _post(
                self._http,
                self._token_url,
                {"grant_type": DEVICE_GRANT, "device_code": self._device_code, "client_id": self._client_id},
            )
            if status == 200:
                return _tokens_of(answer)
            if answer.get("error") == "authorization_pending":
                continue
            if answer.get("error") == "slow_down":
                # asked to wait longer between tries (RFC 8628 §3.5)
                self._interval += 5
                continue
            raise _refusal(status, answer)
        raise BlupintaError(400, "forbidden", ["expired_token: the code expired"])


def start_device_sign_in(
    scope: str,
    *,
    client_id: str = DEVICE_CLIENT_ID,
    auth_origin: str = AUTH_ORIGIN,
    resource: str = API_RESOURCE,
    http: httpx.Client | None = None,
) -> DeviceSignIn:
    """Starts connecting a device with the device flow (RFC 8628): show ``user_code`` and ``verification_uri``, then
    wait on ``tokens()``. ``scope`` is what the app asks (``openid projects:read``...); ``offline_access`` keeps it
    connected."""
    http = http or httpx.Client(timeout=30)
    status, answer = _post(
        http, f"{auth_origin}/oidc/device/auth", {"client_id": client_id, "scope": scope, "resource": resource}
    )
    if status != 200 or "device_code" not in answer:
        raise _refusal(status, answer)
    return DeviceSignIn(http, f"{auth_origin}/oidc/token", client_id, answer)


def refresh_tokens(
    refresh_token: str,
    *,
    client_id: str,
    auth_origin: str = AUTH_ORIGIN,
    http: httpx.Client | None = None,
) -> Tokens:
    """New tokens from a refresh token, for an app that asked ``offline_access``."""
    http = http or httpx.Client(timeout=30)
    status, answer = _post(
        http,
        f"{auth_origin}/oidc/token",
        {"grant_type": "refresh_token", "refresh_token": refresh_token, "client_id": client_id},
    )
    if status != 200:
        raise _refusal(status, answer)
    tokens = _tokens_of(answer)
    # a refresh token may be given once: the old one goes on when none comes back
    if tokens.refresh_token is None:
        tokens = Tokens(tokens.access_token, refresh_token, tokens.expires_at, tokens.scope, tokens.id_token)
    return tokens


class TokenKeeper:
    """The client's ``token``: the access token while it lasts, refreshed a minute before it expires, the new tokens
    handed to ``on_tokens`` to keep (they replace the old ones, a refresh token included)."""

    def __init__(
        self,
        tokens: Tokens,
        *,
        client_id: str,
        on_tokens: Callable[[Tokens], None] | None = None,
        auth_origin: str = AUTH_ORIGIN,
        http: httpx.Client | None = None,
    ) -> None:
        self.tokens = tokens
        self._client_id = client_id
        self._on_tokens = on_tokens
        self._auth_origin = auth_origin
        self._http = http
        self._lock = threading.Lock()

    def __call__(self) -> str:
        # one refresh for every thread waiting on it
        with self._lock:
            if self.tokens.expires_at - time.time() > 60 or not self.tokens.refresh_token:
                return self.tokens.access_token
            self.tokens = refresh_tokens(
                self.tokens.refresh_token, client_id=self._client_id, auth_origin=self._auth_origin, http=self._http
            )
            if self._on_tokens:
                self._on_tokens(self.tokens)
            return self.tokens.access_token
