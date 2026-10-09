from enum import Enum


class ProductManifestBindingsItemKind(str, Enum):
    APPLIANCE = "appliance"
    COVER = "cover"
    LIGHT = "light"
    MEDIA = "media"
    SENSOR = "sensor"

    def __str__(self) -> str:
        return str(self.value)
