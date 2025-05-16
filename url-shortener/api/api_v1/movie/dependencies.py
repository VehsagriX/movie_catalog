from fastapi import HTTPException, status

from .crud import MOVIES


def get_movie_by_id(movie_id: int):
    movie = next((movie for movie in MOVIES if movie.movie_id == movie_id), None)
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {movie_id!r} Not Found",
    )
