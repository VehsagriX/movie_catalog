from typing import Annotated

from fastapi import APIRouter, Depends
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


@router.get("/{id}/", response_model=Movie)
def read_movie_by_id(movie: Annotated[Movie, Depends(get_movie_by_id)]):
    return movie
