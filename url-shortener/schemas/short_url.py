from pydantic import BaseModel


class ShortUrlBase(BaseModel):
    target_url: str  # целевая ссылка
    slug: str  # это -,_, цифры и буквы латинские


class ShortUrl(ShortUrlBase):
    """
    Модель сокращенной ссылки
    """
