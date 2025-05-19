from pydantic import BaseModel

from schemas import Movie, MovieCreate, MovieUpdate


class Storage(BaseModel):
    movies_storage: dict[str, Movie] = {}

    def get_all_movies(self) -> list[Movie]:
        return list(self.movies_storage.values())

    def get_movie_by_slug(self, slug: str) -> Movie | None:
        return self.movies_storage.get(slug)

    def create_movie(self, movie_create: MovieCreate) -> Movie:
        movie = Movie(**movie_create.model_dump())
        self.movies_storage[movie.slug] = movie
        return movie

    def delete_by_slug(self, slug: str) -> None:
        self.movies_storage.pop(slug, None)

    def delete(self, movie: Movie) -> None:
        self.delete_by_slug(movie.slug)

    def update(self, movie: Movie, update_movie: MovieUpdate) -> Movie:
        for key_name, value in update_movie:
            setattr(movie, key_name, value)
        return movie


movie_storage = Storage()

movie_storage.create_movie(
    MovieCreate(
        slug="last",
        title="Last of Us",
        description="Last of Us is best movies in last years",
        year=2022,
    )
)

movie_storage.create_movie(
    MovieCreate(
        slug="sniper",
        title="American Sniper",
        description="After serving in Iraq for years,"
        "Chris Kyle, a lethal US sniper, returns home to his wife and son."
        "However, he cannot cope with the traumatic experiences of war,"
        "affecting his life and relationships.",
        year=2014,
    )
)

movie_storage.create_movie(
    MovieCreate(
        slug="harry",
        title="Harry Potter and the Prisoner of Azkaban",
        description="Harry Potter's third year at Hogwarts turns out to be eventful as he gets"
        "tutored by Professor Lupin, a Defence Against the Dark Arts teacher,"
        "and tackles Sirius Black, a vengeful fugitive prisoner.",
        year=2005,
    )
)
