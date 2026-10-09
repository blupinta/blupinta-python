from enum import Enum


class NumberOptionUnit(str, Enum):
    COUNT = "count"
    DEGREES = "degrees"
    M = "m"

    def __str__(self) -> str:
        return str(self.value)
