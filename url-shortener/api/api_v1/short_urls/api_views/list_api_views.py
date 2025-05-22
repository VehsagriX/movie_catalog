from fastapi import APIRouter, status, BackgroundTasks

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
    background_tasks: BackgroundTasks,
) -> ShortUrl:
    background_tasks.add_task(storage.save_state)
    # add background task
    return storage.create(short_url_create)
