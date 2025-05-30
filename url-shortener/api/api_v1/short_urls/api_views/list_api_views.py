from fastapi import APIRouter, status, Depends

from api.api_v1.short_urls.dependencies import save_storage_state

from schemas import ShortUrl, ShortUrlCreate, ShortUrlRead
from api.api_v1.short_urls.crud import storage

router = APIRouter(
    prefix="/short-url",
    tags=["Short URLs"],
    dependencies=[
        Depends(save_storage_state),
    ],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Only for unsafe methods",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid credentials.",
                    },
                }
            },
        },
    },
)


@router.get("/", response_model=list[ShortUrlRead])
def read_short_urls_list():
    return storage.get()


@router.post(
    "/",
    response_model=ShortUrlRead,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(
    short_url_create: ShortUrlCreate,
) -> ShortUrl:

    return storage.create(short_url_create)
