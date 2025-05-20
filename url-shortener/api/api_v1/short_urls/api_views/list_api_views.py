from fastapi import APIRouter, status

from schemas import ShortUrl, ShortUrlCreate, ShortUrlRead

from api.api_v1.short_urls.crud import storage

router = APIRouter(
    prefix="/short-url",
    tags=["Short URLs"],
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
):
    return storage.create(short_url_create)
