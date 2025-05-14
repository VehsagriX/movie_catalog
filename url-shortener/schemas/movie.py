from enum import unique

from pydantic import BaseModel


class MovieBase(BaseModel):
    movie_id: int
    title: str
    description: str
    year: int


class Movie(MovieBase):
    """
    Модель фильма
    """

    pass
