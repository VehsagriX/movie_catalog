from fastapi import HTTPException, status

from .crud import MOVIES


def get_movie_by_id(slug: str):
    movie = next((movie for movie in MOVIES if movie.slug == slug.lower()), None)
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {slug!r} Not Found",
    )
