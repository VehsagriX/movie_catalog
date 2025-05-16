from typing import Annotated
from annotated_types import MinLen, MaxLen
from fastapi import Depends, APIRouter, status, Form
from pydantic import AnyHttpUrl

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


@router.post(
    "/",
    response_model=ShortUrl,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(
    target_url: Annotated[AnyHttpUrl, Form()],
    slug: Annotated[str, MinLen(3), MaxLen(10), Form()],
):
    return ShortUrl(target_url=target_url, slug=slug)


@router.get("/{slug}/", response_model=ShortUrl)
def read_short_url_detail(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_urls),
    ],
) -> ShortUrl:
    return url
