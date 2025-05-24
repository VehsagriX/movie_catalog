from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from api.api_v1.short_urls.crud import storage
from api.api_v1.short_urls.dependencies import prefetch_short_urls
from schemas import ShortUrl, ShortUrlUpdate, ShortUrlPartialUpdate, ShortUrlRead

router = APIRouter(
    prefix="/{slug}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Short URL not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "URL 'slug' not found",
                    },
                },
            },
        },
    },
)

ShortUrlBySlug = Annotated[
    ShortUrl,
    Depends(prefetch_short_urls),
]


@router.get("/", response_model=ShortUrlRead)
def read_short_url_detail(
    url: ShortUrlBySlug,
) -> ShortUrl:
    return url


@router.put("/", response_model=ShortUrlRead)
def update_short_url_detail(
    url: ShortUrlBySlug,
    short_url_in: ShortUrlUpdate,
) -> ShortUrl:
    return storage.update(short_url=url, short_url_in=short_url_in)


@router.patch("/", response_model=ShortUrlRead)
def partial_update_short_url_detail(
    url: ShortUrlBySlug,
    short_url_in: ShortUrlPartialUpdate,
):
    return storage.update_partial(short_url=url, short_url_in=short_url_in)


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_short_url(
    url: ShortUrlBySlug,
) -> None:
    storage.delete(short_url=url)
