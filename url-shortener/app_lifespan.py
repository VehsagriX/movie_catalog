from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.api_v1.movie.crud import movie_storage
from api.api_v1.short_urls.crud import storage


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Действия до запуска приложения.
    storage.init_url_short_storage_from_state()
    movie_storage.init_movie_storage_from_state()
    # Ставим эту функцию на паузу на время работы приложения
    yield
    # Выполняем завершение работы,
    # Закрываем соединения, финально сохраняем файлы.
