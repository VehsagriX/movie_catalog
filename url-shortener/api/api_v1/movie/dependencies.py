from fastapi import HTTPException, status

from schemas import Movie
from .crud import movie_storage


def get_movie_by_slug(slug: str) -> Movie:
    movie: Movie | None = movie_storage.get_movie_by_slug(slug=slug)
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {slug!r} Not Found",
    )
