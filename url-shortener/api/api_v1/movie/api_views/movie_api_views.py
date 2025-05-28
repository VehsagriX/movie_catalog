from fastapi import APIRouter, status, Depends

from api.api_v1.global_depensities import user_basic_auth_required, api_token_required
from schemas import Movie, MovieCreate, MovieRead

from api.api_v1.movie.crud import movie_storage
from api.api_v1.movie.dependencies import depends_save_movie_storage

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
    dependencies=[
        Depends(depends_save_movie_storage),
        Depends(user_basic_auth_required),
        # Depends(api_token_required),
    ],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Only for unsafe methods",
            "content": {
                "application/json": {"example": {"detail": "Invalid API token"}}
            },
        },
    },
)


@router.get("/", response_model=list[MovieRead])
def read_movies_list():
    return movie_storage.get_all_movies()


@router.post("/", response_model=MovieRead, status_code=status.HTTP_201_CREATED)
def create_movie(
    movie_create: MovieCreate,
) -> Movie:
    return movie_storage.create_movie(movie_create)
