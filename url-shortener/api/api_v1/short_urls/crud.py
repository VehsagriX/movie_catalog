from pydantic import BaseModel, AnyHttpUrl

from schemas import ShortUrl, ShortUrlCreate, ShortUrlUpdate, ShortUrlPartialUpdate


class ShortUrlsStorage(BaseModel):
    slug_to_short_url: dict[str, ShortUrl] = {}

    def get(self) -> list[ShortUrl]:
        return list(self.slug_to_short_url.values())

    def get_by_slug(self, slug) -> ShortUrl | None:
        return self.slug_to_short_url.get(slug)

    def create(self, short_url_create: ShortUrlCreate) -> ShortUrl:
        short_url = ShortUrl(
            **short_url_create.model_dump(),
        )
        self.slug_to_short_url[short_url.slug] = short_url
        return short_url

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_short_url.pop(slug, None)

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

        return short_url

    def update_partial(
        self,
        short_url: ShortUrl,
        short_url_in: ShortUrlPartialUpdate,
    ) -> ShortUrl:
        for field, value in short_url_in.model_dump(exclude_unset=True).items():
            setattr(short_url, field, value)
        return short_url


storage = ShortUrlsStorage()
storage.create(
    ShortUrlCreate(
        target_url=AnyHttpUrl("https://www.example.com"),
        slug="example",
    )
)
storage.create(
    ShortUrlCreate(
        target_url=AnyHttpUrl("https://www.google.com"),
        slug="search",
    )
)
