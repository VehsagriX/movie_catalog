from pydantic import BaseModel, AnyHttpUrl


class ShortUrlBase(BaseModel):
    target_url: AnyHttpUrl  # целевая ссылка
    slug: str  # это -,_, цифры и буквы латинские


class ShortUrl(ShortUrlBase):
    """
    Модель сокращенной ссылки
    """
