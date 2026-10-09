from enum import Enum


class ClearanceSide(str, Enum):
    BACK = "back"
    FRONT = "front"
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
