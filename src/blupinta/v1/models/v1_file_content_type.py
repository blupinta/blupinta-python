from enum import Enum


class V1FileContentType(str, Enum):
    APPLICATIONPDF = "application/pdf"
    IMAGEJPEG = "image/jpeg"
    IMAGEPNG = "image/png"
    IMAGEWEBP = "image/webp"

    def __str__(self) -> str:
        return str(self.value)
