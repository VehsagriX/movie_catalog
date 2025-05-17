from typing import Annotated

from fastapi import Depends, APIRouter
from starlette.responses import RedirectResponse

from .api_v1.short_urls.dependencies import prefetch_short_urls
from schemas import ShortUrl


router = APIRouter(
    prefix="/r",
    tags=["Redirect"],
)


@router.get("/{slug}")
@router.get("/{slug}/")
def redirect__short_url(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_urls),
    ],
) -> RedirectResponse:

    return RedirectResponse(url=str(url.target_url))
