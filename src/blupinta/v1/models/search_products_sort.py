from enum import Enum


class SearchProductsSort(str, Enum):
    LARGEST = "largest"
    NAME = "name"
    RELEVANCE = "relevance"
    SMALLEST = "smallest"

    def __str__(self) -> str:
        return str(self.value)
