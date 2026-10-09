"""Checking that a webhook's post came from Blupinta: its ``Blupinta-Signature`` header is ``t=<seconds>,v1=<hex>``,
the HMAC-SHA256 of ``<t>.<body>`` with the webhook's secret. A post signed with another secret, changed on the way, or
older than the tolerance (a replay) is refused."""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any


def is_signed_webhook(
    body: bytes | str, signature: str | None, secret: str, *, tolerance: float = 300, now: float | None = None
) -> bool:
    """Whether ``body`` (the post's raw bytes, before any parsing) was signed by Blupinta with ``secret`` within the
    last ``tolerance`` seconds."""
    raw = body.encode() if isinstance(body, str) else body
    parts = dict(part.split("=", 1) for part in (signature or "").split(",") if "=" in part)
    if not parts.get("t", "").isdigit() or "v1" not in parts:
        return False
    t = int(parts["t"])
    if abs((now if now is not None else time.time()) - t) > tolerance:
        return False
    expected = hmac.new(secret.encode(), f"{t}.".encode() + raw, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, parts["v1"])


def read_webhook(body: bytes | str, signature: str | None, secret: str, **options: Any) -> dict[str, Any] | None:
    """The body of a post whose signature holds; ``None`` when it doesn't, so the app answers 400 and ignores it."""
    return json.loads(body) if is_signed_webhook(body, signature, secret, **options) else None
