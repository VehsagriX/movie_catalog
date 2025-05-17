from fastapi import HTTPException, status

from schemas import ShortUrl

from .crud import storage


def prefetch_short_urls(slug: str) -> ShortUrl:
    url: ShortUrl | None = storage.get_by_slug(slug)

    if url:
        return url
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"URL {slug!r} Not found",
    )
