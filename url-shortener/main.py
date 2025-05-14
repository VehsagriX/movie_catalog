from typing import Annotated


from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.responses import RedirectResponse
from schemas import ShortUrl, Movie

app = FastAPI(
    title="URL Shortener",
)

SHORT_URLS = [
    ShortUrl(
        target_url="https://www.example.com",
        slug="example",
    ),
    ShortUrl(
        target_url="https://www.google.com",
        slug="search",
    ),
]


MOVIES = [
    Movie(
        movie_id=1,
        title="Harry Potter and the Prisoner of Azkaban",
        description="""Harry Potter's third year at Hogwarts turns out to be eventful as he gets 
tutored by Professor Lupin, a Defence Against the Dark Arts teacher, 
and tackles Sirius Black, a vengeful fugitive prisoner.""",
        year=2005,
    ),
    Movie(
        movie_id=2,
        title="American Sniper",
        description="""After serving in Iraq for years, 
Chris Kyle, a lethal US sniper, returns home to his wife and son.
However, he cannot cope with the traumatic experiences of war,
affecting his life and relationships.""",
        year=2014,
    ),
    Movie(
        movie_id=3,
        title="Last of Us",
        description="Last of Us is best movies in last years",
        year=2022,
    ),
]


@app.get("/")
def read_root(request: Request, name: str = "World"):
    docs_url = request.url.replace(path="/docs", query="")
    return {
        "message": f"Hello {name}",
        "docs": docs_url,
    }


@app.get("/short-url/", response_model=list[ShortUrl])
def read_short_urls_list():
    return SHORT_URLS


def prefetch_short_urls(slug: str) -> ShortUrl:
    url: ShortUrl | None = next(
        (url for url in SHORT_URLS if url.slug == slug),
        None,
    )
    if url:
        return url
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"URL {slug!r} Not found",
    )


@app.get("/r/{slug}")
@app.get("/r/{slug}/")
def redirect__short_url(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_urls),
    ],
) -> RedirectResponse:

    return RedirectResponse(url=url.target_url)


@app.get("/short-urls/{slug}/", response_model=ShortUrl)
def read_short_url_detail(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_urls),
    ],
) -> ShortUrl:
    return url


@app.get("/movies/", response_model=list[Movie])
def read_movies_list():
    return MOVIES


@app.get("/movies/{id}/", response_model=Movie)
def read_movie_by_id(id: int):
    movie = next((movie for movie in MOVIES if movie.movie_id == id), None)
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {id!r} Not Found",
    )
