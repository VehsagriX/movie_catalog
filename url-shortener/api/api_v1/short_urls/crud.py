import logging

from pydantic import BaseModel, ValidationError
from core.config import SHORT_URL_STORAGE_FILE
from schemas import ShortUrl, ShortUrlCreate, ShortUrlUpdate, ShortUrlPartialUpdate


logger = logging.getLogger(__name__)


class ShortUrlsStorage(BaseModel):
    slug_to_short_url: dict[str, ShortUrl] = {}

    def save_state(self) -> None:
        SHORT_URL_STORAGE_FILE.write_text(self.model_dump_json(indent=2))
        logger.info("Saved short url storage file")

    @classmethod
    def from_state(cls) -> "ShortUrlsStorage":
        if not SHORT_URL_STORAGE_FILE.exists():
            logger.info("Short url storage file dosen't exist")

            return ShortUrlsStorage()
        return cls.model_validate_json(SHORT_URL_STORAGE_FILE.read_text())

    def init_url_short_storage_from_state(self) -> None:
        try:
            data = ShortUrlsStorage.from_state()
        except ValidationError:
            self.save_state()
            logger.warning("Rewritten storage file due to validation error.")
            return

        # мы обновляем свойство напрямую
        # если будут новые свойства,
        # то их тоже надо обновить.
        self.slug_to_short_url.update(data.slug_to_short_url)
        logger.warning("Recovered data from storage file")

    def get(self) -> list[ShortUrl]:
        return list(self.slug_to_short_url.values())

    def get_by_slug(self, slug) -> ShortUrl | None:
        return self.slug_to_short_url.get(slug)

    def create(self, short_url_create: ShortUrlCreate) -> ShortUrl:
        short_url = ShortUrl(
            **short_url_create.model_dump(),
        )
        self.slug_to_short_url[short_url.slug] = short_url
        self.save_state()
        return short_url

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_short_url.pop(slug, None)
        self.save_state()

    def delete(self, short_url: ShortUrl) -> None:
        self.delete_by_slug(short_url.slug)

    def update(
        self,
        short_url: ShortUrl,
        short_url_in: ShortUrlUpdate,
    ) -> ShortUrl:
        # 1 вариант
        # updated_short_url = short_url.model_copy(
        #     update=short_url_in.model_dump(),
        # )
        # self.slug_to_short_url[short_url.slug] = updated_short_url

        # 2 вариант
        for field, value in short_url_in:
            setattr(short_url, field, value)

        self.save_state()

        return short_url

    def update_partial(
        self,
        short_url: ShortUrl,
        short_url_in: ShortUrlPartialUpdate,
    ) -> ShortUrl:
        for field, value in short_url_in.model_dump(exclude_unset=True).items():
            setattr(short_url, field, value)

        self.save_state()

        return short_url


storage = ShortUrlsStorage()
