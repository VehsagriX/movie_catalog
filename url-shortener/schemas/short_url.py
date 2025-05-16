from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, AnyHttpUrl


class ShortUrlBase(BaseModel):
    target_url: AnyHttpUrl  # целевая ссылка
    slug: str  # это -,_, цифры и буквы латинские


class ShortUrlCreate(ShortUrlBase):
    """
    Модель для создания сокращенной ссылки
    """

    slug: Annotated[str, MinLen(3), MaxLen(10)]


class ShortUrl(ShortUrlBase):
    """
    Модель сокращенной ссылки
    """
