from enum import Enum


class V1DeviceKind(str, Enum):
    CLIMATE = "climate"
    COVER = "cover"
    LIGHT = "light"
    MEDIA = "media"
    SENSOR = "sensor"
    SWITCH = "switch"

    def __str__(self) -> str:
        return str(self.value)
