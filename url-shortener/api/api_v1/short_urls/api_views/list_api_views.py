from fastapi import APIRouter, status, Depends

from api.api_v1.short_urls.dependencies import save_storage_state
from api.api_v1.global_depensities import api_token_required
from schemas import ShortUrl, ShortUrlCreate, ShortUrlRead
from api.api_v1.short_urls.crud import storage

router = APIRouter(
    prefix="/short-url",
    tags=["Short URLs"],
    dependencies=[Depends(save_storage_state)],
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
    _=Depends(api_token_required),  # если переменная зависимости не нужна!
) -> ShortUrl:

    return storage.create(short_url_create)
