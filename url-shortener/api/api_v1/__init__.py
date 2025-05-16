from fastapi import APIRouter

from .short_urls.api_views import router as short_url_router
from .movie.api_views import router as movie_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(short_url_router)
router.include_router(movie_router)
