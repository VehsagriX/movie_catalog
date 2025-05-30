from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.api_v1.movie.crud import movie_storage
from api.api_v1.movie.dependencies import get_movie_by_slug
from schemas import Movie, MovieUpdate, MoviePartialUpdate, MovieRead

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

MovieBySlug = Annotated[Movie, Depends(get_movie_by_slug)]


@router.get("/", response_model=MovieRead)
def read_movie_by_id(movie: MovieBySlug):
    return movie


@router.put("/", response_model=MovieRead)
def update_movie(
    movie: MovieBySlug,
    movie_update: MovieUpdate,
):
    return movie_storage.update(movie=movie, update_movie=movie_update)


@router.patch("/", response_model=MovieRead)
def partial_update_movie(
    movie: MovieBySlug,
    movie_update: MoviePartialUpdate,
):
    return movie_storage.partial_update(movie=movie, update_movie=movie_update)


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: MovieBySlug,
) -> None:
    movie_storage.delete(movie)
