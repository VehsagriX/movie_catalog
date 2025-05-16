import random
from typing import Annotated
from annotated_types import Len
from fastapi import APIRouter, Depends, status, Form
from schemas import Movie

from .crud import MOVIES
from .dependencies import get_movie_by_id

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get("/", response_model=list[Movie])
def read_movies_list():
    return MOVIES


@router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_movie(
    title: Annotated[str, Len(min_length=4, max_length=30), Form()],
    description: Annotated[str, Form()],
    year: Annotated[int, Form()],
):
    movie_id = random.randint(1, 100)
    return Movie(
        movie_id=movie_id,
        title=title,
        description=description,
        year=year,
    )


@router.get("/{id}/", response_model=Movie)
def read_movie_by_id(movie: Annotated[Movie, Depends(get_movie_by_id)]):
    return movie
