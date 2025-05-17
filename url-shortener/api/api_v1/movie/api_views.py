from typing import Annotated
from fastapi import APIRouter, Depends, status
from schemas import Movie, MovieCreate

from .crud import movie_storage
from .dependencies import get_movie_by_id

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get("/", response_model=list[Movie])
def read_movies_list():
    return movie_storage.get_all_movies()


@router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_movie(
    movie_create: MovieCreate,
):

    return movie_storage.create_movie(movie_create)


@router.get("/{slug}/", response_model=Movie)
def read_movie_by_id(movie: Annotated[Movie, Depends(get_movie_by_id)]):
    return movie


@router.delete(
    "/{slug}/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie 'slug' not found",
                    },
                },
            },
        },
    },
)
def delete_movie(movie: Annotated[Movie, Depends(get_movie_by_id)]) -> None:
    movie_storage.delete(movie)
