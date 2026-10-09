from enum import Enum


class V1ProductLinksItemKind(str, Enum):
    MANUAL = "manual"
    PRODUCT = "product"
    SHOP = "shop"

    def __str__(self) -> str:
        return str(self.value)
