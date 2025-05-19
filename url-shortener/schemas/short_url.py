from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, AnyHttpUrl


class ShortUrlBase(BaseModel):
    target_url: AnyHttpUrl  # целевая ссылка
    description: Annotated[str, MaxLen(200)] = ""


class ShortUrlCreate(ShortUrlBase):
    """
    Модель для создания сокращенной ссылки
    """

    slug: Annotated[str, MinLen(3), MaxLen(10)]


class ShortUrlUpdate(ShortUrlBase):
    """Модель для обновления информации о сокращенной ссылки"""
    description: Annotated[str, MaxLen(200)]

class ShortUrl(ShortUrlBase):
    """
    Модель сокращенной ссылки
    """

    slug: str  # это -,_, цифры и буквы латинские
