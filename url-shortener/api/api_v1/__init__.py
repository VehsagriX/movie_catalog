from fastapi import APIRouter, Depends, status

from .short_urls.api_views import router as short_url_router
from .movie.api_views import router as movie_router
from .global_depensities import api_token_or_user_basic_auth_required_for_unsafe_methods

router = APIRouter(
    prefix="/v1",
    dependencies=[
        Depends(api_token_or_user_basic_auth_required_for_unsafe_methods),
    ],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Only for unsafe methods",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid API token or basic auth credentials"
                    },
                }
            },
        },
    },
)


router.include_router(short_url_router)
router.include_router(movie_router)
