from enum import Enum


class SearchProductsLanguage(str, Enum):
    EN = "en"
    IT = "it"

    def __str__(self) -> str:
        return str(self.value)
