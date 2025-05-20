from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, AnyHttpUrl


DescriptionDetails = Annotated[str, MaxLen(200)]


class ShortUrlBase(BaseModel):
    target_url: AnyHttpUrl  # целевая ссылка
    description: DescriptionDetails = ""


class ShortUrlCreate(ShortUrlBase):
    """
    Модель для создания сокращенной ссылки
    """

    slug: Annotated[str, MinLen(3), MaxLen(10)]


class ShortUrlUpdate(ShortUrlBase):
    """Модель для полного (PUT) обновления информации о сокращенной ссылки"""

    description: DescriptionDetails


class ShortUrlPartialUpdate(ShortUrlBase):
    """Модель для частичного (Patch) обновления сокращенной ссылки"""

    target_url: AnyHttpUrl | None = None
    description: DescriptionDetails | None = None


class ShortUrlRead(ShortUrlBase):
    """Модель для чтения данных по сокращенной ссылке"""

    slug: str


class ShortUrl(ShortUrlBase):
    """
    Модель сокращенной ссылки
    """

    slug: str  # это -,_, цифры и буквы латинские
    visits: int = 42
