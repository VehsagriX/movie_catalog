from typing import Annotated
from annotated_types import Len
from pydantic import BaseModel


class MovieBase(BaseModel):
    movie_id: int
    title: str
    description: str
    year: int


class MovieCreate(BaseModel):
    """Модель создания фильма"""

    title: Annotated[str, Len(min_length=4, max_length=30)]
    description: str
    year: int


class Movie(MovieBase):
    """
    Модель фильма
    """

    pass
