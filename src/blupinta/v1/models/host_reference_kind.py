from enum import Enum


class HostReferenceKind(str, Enum):
    AREA = "area"
    AWNING = "awning"
    ITEM = "item"
    LEVEL = "level"
    LIGHT = "light"
    OPENING = "opening"
    PLAN = "plan"
    PLATE = "plate"
    PRESENTATION = "presentation"
    ROOM = "room"
    STAIR = "stair"
    WALL = "wall"

    def __str__(self) -> str:
        return str(self.value)
