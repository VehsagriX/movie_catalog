from typing import Annotated

from fastapi import APIRouter, Depends, BackgroundTasks
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


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_short_url(
    url: ShortUrlBySlug,
    background_tasks: BackgroundTasks,
) -> None:
    background_tasks.add_task(storage.save_state)
    storage.delete(short_url=url)


@router.put("/", response_model=ShortUrlRead)
def update_short_url_detail(
    url: ShortUrlBySlug,
    short_url_in: ShortUrlUpdate,
    background_tasks: BackgroundTasks,
) -> ShortUrl:
    background_tasks.add_task(storage.save_state)
    return storage.update(short_url=url, short_url_in=short_url_in)


@router.patch("/", response_model=ShortUrlRead)
def partial_update_short_url_detail(
    url: ShortUrlBySlug,
    short_url_in: ShortUrlPartialUpdate,
    background_tasks: BackgroundTasks,
):
    background_tasks.add_task(storage.save_state)
    return storage.update_partial(short_url=url, short_url_in=short_url_in)
