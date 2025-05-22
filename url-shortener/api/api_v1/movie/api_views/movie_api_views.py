from fastapi import APIRouter, status, BackgroundTasks, Depends
from schemas import Movie, MovieCreate, MovieRead

from api.api_v1.movie.crud import movie_storage
from api.api_v1.movie.dependencies import depends_save_movie_storage

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
    dependencies=[Depends(depends_save_movie_storage)],
)


@router.get("/", response_model=list[MovieRead])
def read_movies_list():
    return movie_storage.get_all_movies()


@router.post("/", response_model=MovieRead, status_code=status.HTTP_201_CREATED)
def create_movie(
    movie_create: MovieCreate,
) -> Movie:
    return movie_storage.create_movie(movie_create)
