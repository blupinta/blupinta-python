from enum import Enum


class SearchProductsMount(str, Enum):
    BUILT_IN = "built-in"
    CEILING = "ceiling"
    FLOOR = "floor"
    SURFACE = "surface"
    WALL = "wall"

    def __str__(self) -> str:
        return str(self.value)
