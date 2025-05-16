from typing import Annotated

from fastapi import Depends, APIRouter, status, Form


from schemas import ShortUrl
from schemas.short_url import ShortUrlCreate

from .dependencies import prefetch_short_urls
from .crud import SHORT_URLS


router = APIRouter(
    prefix="/short-url",
    tags=["Short URLs"],
)


@router.get("/", response_model=list[ShortUrl])
def read_short_urls_list():
    return SHORT_URLS


@router.post(
    "/",
    response_model=ShortUrl,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(
    short_url: ShortUrlCreate,
):
    return ShortUrl(**short_url.model_dump())


@router.get("/{slug}/", response_model=ShortUrl)
def read_short_url_detail(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_urls),
    ],
) -> ShortUrl:
    return url
