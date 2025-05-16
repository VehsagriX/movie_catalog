from typing import Annotated

from fastapi import Depends, APIRouter
from schemas import ShortUrl

from .dependencies import prefetch_short_urls
from .crud import SHORT_URLS


router = APIRouter(
    prefix="/short-url",
    tags=["Short URLs"],
)


@router.get("/", response_model=list[ShortUrl])
def read_short_urls_list():
    return SHORT_URLS


@router.get("/{slug}/", response_model=ShortUrl)
def read_short_url_detail(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_urls),
    ],
) -> ShortUrl:
    return url
