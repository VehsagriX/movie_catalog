from typing import Annotated

from fastapi import Depends, APIRouter, status, Form


from schemas import ShortUrl
from schemas.short_url import ShortUrlCreate

from .dependencies import prefetch_short_urls
from .crud import storage


router = APIRouter(
    prefix="/short-url",
    tags=["Short URLs"],
)


@router.get("/", response_model=list[ShortUrl])
def read_short_urls_list():
    return storage.get()


@router.post(
    "/",
    response_model=ShortUrl,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(
    short_url_create: ShortUrlCreate,
):
    return storage.create(short_url_create)


@router.get("/{slug}/", response_model=ShortUrl)
def read_short_url_detail(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_urls),
    ],
) -> ShortUrl:
    return url
