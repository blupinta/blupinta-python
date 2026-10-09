from enum import Enum


class RecipePartType0Shape(str, Enum):
    BOX = "box"
    CYLINDER = "cylinder"

    def __str__(self) -> str:
        return str(self.value)
