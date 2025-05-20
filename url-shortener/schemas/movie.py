from typing import Annotated
from annotated_types import Len, MinLen, MaxLen
from pydantic import BaseModel


TitleStr = Annotated[str, Len(min_length=4, max_length=100)]


class MovieBase(BaseModel):

    title: str
    description: str = ""
    year: int


class MovieCreate(BaseModel):
    """Модель создания фильма"""

    slug: Annotated[str, MinLen(3), MaxLen(10)]
    title: TitleStr
    description: str
    year: int


class MovieUpdate(MovieBase):
    """Модель для полного (PUT) обновления фильма"""

    pass


class MoviePartialUpdate(MovieBase):
    """Модель для частичного (Patch) обновления фильма"""

    title: TitleStr | None = None
    description: str | None = None
    year: int | None = None


class Movie(MovieBase):
    """
    Модель фильма
    """

    slug: str
