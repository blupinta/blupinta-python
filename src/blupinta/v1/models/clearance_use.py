from enum import Enum


class ClearanceUse(str, Enum):
    ACCESS = "access"
    APPLIANCE = "appliance"
    DOORS = "doors"
    DRAWERS = "drawers"
    SEAT = "seat"

    def __str__(self) -> str:
        return str(self.value)
