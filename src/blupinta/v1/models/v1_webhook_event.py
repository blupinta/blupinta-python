from enum import Enum


class V1WebhookEvent(str, Enum):
    ACCESS_REVOKED = "access.revoked"
    REVISION_SAVED = "revision.saved"

    def __str__(self) -> str:
        return str(self.value)
