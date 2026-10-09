"""A webhook's signature: Blupinta's holds, a changed body, another secret or an old post doesn't."""

import hashlib
import hmac

from blupinta import is_signed_webhook, read_webhook

BODY = b'{"event":"revision.saved"}'


def signed(body: bytes, secret: str, t: int) -> str:
    return f"t={t},v1={hmac.new(secret.encode(), f'{t}.'.encode() + body, hashlib.sha256).hexdigest()}"


def test_blupintas_signature_holds_and_nothing_else_does():
    signature = signed(BODY, "secret", 1_000)
    assert is_signed_webhook(BODY, signature, "secret", now=1_000)
    assert read_webhook(BODY, signature, "secret", now=1_000) == {"event": "revision.saved"}
    assert not is_signed_webhook(BODY + b" ", signature, "secret", now=1_000)
    assert not is_signed_webhook(BODY, signature, "other", now=1_000)
    assert not is_signed_webhook(BODY, signature, "secret", now=1_000 + 600)
    assert not is_signed_webhook(BODY, None, "secret")
