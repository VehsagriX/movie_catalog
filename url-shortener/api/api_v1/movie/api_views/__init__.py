__all__ = ("router",)


from .movie_api_views import router
from .details_api_views import router as details_router


router.include_router(details_router)
