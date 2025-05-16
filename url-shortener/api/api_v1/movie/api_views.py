import random
from typing import Annotated
from fastapi import APIRouter, Depends, status
from schemas import Movie, MovieCreate

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
    movie: MovieCreate,
):

    return Movie(**movie.model_dump())


@router.get("/{slug}/", response_model=Movie)
def read_movie_by_id(movie: Annotated[Movie, Depends(get_movie_by_id)]):
    return movie
