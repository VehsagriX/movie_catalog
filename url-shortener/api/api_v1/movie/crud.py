import logging

from pydantic import BaseModel, ValidationError
from core.config import MOVIE_STORAGE_FILE
from schemas import Movie, MovieCreate, MovieUpdate, MoviePartialUpdate


logger = logging.getLogger(__name__)


class Storage(BaseModel):
    movies_storage: dict[str, Movie] = {}

    def save_state(self):

        MOVIE_STORAGE_FILE.write_text(self.model_dump_json(indent=2))
        logger.info("Успешно сохранена история файла.")

    @classmethod
    def from_state(cls):
        if not MOVIE_STORAGE_FILE.exists():
            return Storage()
        return Storage.model_validate_json(MOVIE_STORAGE_FILE.read_text())

    def init_movie_storage_from_state(self) -> None:
        try:
            data = Storage.from_state()

        except ValidationError:
            self.save_state()
            logger.warning(
                "Ошибка чтения файла: %s. Файл %s будет перезаписан",
                MOVIE_STORAGE_FILE,
                MOVIE_STORAGE_FILE,
            )
            return
        # мы обновляем свойство напрямую
        # если будут новые свойства,
        # то их тоже надо обновить.
        self.movies_storage.update(data.movies_storage)
        logger.warning("Состояние успешно прочитано с диска: %s", MOVIE_STORAGE_FILE)

    def get_all_movies(self) -> list[Movie]:
        return list(self.movies_storage.values())

    def get_movie_by_slug(self, slug: str) -> Movie | None:
        return self.movies_storage.get(slug)

    def create_movie(self, movie_create: MovieCreate) -> Movie:
        movie = Movie(**movie_create.model_dump())
        self.movies_storage[movie.slug] = movie

        self.save_state()
        logger.info("Фильм успешно %s создан.", movie.title)
        return movie

    def delete_by_slug(self, slug: str) -> None:
        self.movies_storage.pop(slug, None)
        self.save_state()

    def delete(self, movie: Movie) -> None:
        self.delete_by_slug(movie.slug)

    def update(self, movie: Movie, update_movie: MovieUpdate) -> Movie:
        for key_name, value in update_movie:
            setattr(movie, key_name, value)
        self.save_state()
        return movie

    def partial_update(self, movie: Movie, update_movie: MoviePartialUpdate) -> Movie:
        for field, value in update_movie.model_dump(exclude_unset=True).items():
            setattr(movie, field, value)

        self.save_state()
        return movie


movie_storage = Storage()
