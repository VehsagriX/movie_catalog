import logging

from fastapi import HTTPException, status, BackgroundTasks, Request

from core.config import UNSAFE_METHODS
from schemas import Movie
from .crud import movie_storage

logger = logging.getLogger(__name__)


def get_movie_by_slug(slug: str) -> Movie:
    movie: Movie | None = movie_storage.get_movie_by_slug(slug=slug)
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {slug!r} Not Found",
    )


def depends_save_movie_storage(
    request: Request,
    background_task: BackgroundTasks,
):

    yield
    if request.method in UNSAFE_METHODS:
        logger.info("Задали сохраннение данных на диск")
        background_task.add_task(movie_storage.save_state)
