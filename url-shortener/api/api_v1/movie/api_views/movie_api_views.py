from fastapi import APIRouter, status, BackgroundTasks
from schemas import Movie, MovieCreate, MovieRead

from api.api_v1.movie.crud import movie_storage

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get("/", response_model=list[MovieRead])
def read_movies_list():
    return movie_storage.get_all_movies()


@router.post("/", response_model=MovieRead, status_code=status.HTTP_201_CREATED)
def create_movie(
    movie_create: MovieCreate,
    background_tasks: BackgroundTasks,
) -> Movie:
    background_tasks.add_task(movie_storage.save_state)
    return movie_storage.create_movie(movie_create)
