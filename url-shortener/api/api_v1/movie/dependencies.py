from fastapi import HTTPException, status

from .crud import movie_storage


def get_movie_by_id(slug: str):
    movie = movie_storage.find(slug=slug)
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {slug!r} Not Found",
    )
