import logging

from fastapi import HTTPException, status, BackgroundTasks, Request

from schemas import ShortUrl

from .crud import storage

logger = logging.getLogger(__name__)

UNSAFE_METHODS = frozenset(
    {
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    }
)


def prefetch_short_urls(slug: str) -> ShortUrl:
    url: ShortUrl | None = storage.get_by_slug(slug)

    if url:
        return url
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"URL {slug!r} Not found",
    )


def save_storage_state(
    background_tasks: BackgroundTasks,
    request: Request,
):
    # сначала код до входа внутрь view функции
    yield
    # код после покидания view функции
    if request.method in UNSAFE_METHODS:
        logger.info("Add background tasks to save storage")
        background_tasks.add_task(storage.save_state)
