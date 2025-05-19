from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.api_v1.movie.crud import movie_storage
from api.api_v1.movie.dependencies import get_movie_by_id
from schemas import Movie


router = APIRouter(
    prefix="/{slug}",
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


@router.get("/", response_model=Movie)
def read_movie_by_id(movie: Annotated[Movie, Depends(get_movie_by_id)]):
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(movie: Annotated[Movie, Depends(get_movie_by_id)]) -> None:
    movie_storage.delete(movie)
