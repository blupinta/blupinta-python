"""The official SDK for Blupinta's public API, https://api.blupinta.app/v1: every operation of the API (``blupinta.v1``,
generated from its OpenAPI document) called through ``Blupinta``, the person signed in with the device flow, a home
followed as its versions are saved, webhooks checked. The guide: https://docs.blupinta.app/reference/public-api/"""

from .auth import DeviceSignIn, TokenKeeper, Tokens, refresh_tokens, start_device_sign_in
from .client import Blupinta
from .errors import BlupintaError
from .watch import watch_home
from .webhooks import is_signed_webhook, read_webhook

__version__ = "0.1.0"

__all__ = [
    "Blupinta",
    "BlupintaError",
    "DeviceSignIn",
    "TokenKeeper",
    "Tokens",
    "is_signed_webhook",
    "read_webhook",
    "refresh_tokens",
    "start_device_sign_in",
    "watch_home",
]
