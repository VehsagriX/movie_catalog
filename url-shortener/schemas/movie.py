from typing import Annotated
from annotated_types import Len, MinLen, MaxLen
from pydantic import BaseModel


class MovieBase(BaseModel):

    title: str
    description: str = ""
    year: int


class MovieCreate(BaseModel):
    """Модель создания фильма"""

    slug: Annotated[str, MinLen(3), MaxLen(10)]
    title: Annotated[str, Len(min_length=4, max_length=100)]
    description: str
    year: int


class MovieUpdate(MovieBase):
    pass


class Movie(MovieBase):
    """
    Модель фильма
    """

    slug: str
