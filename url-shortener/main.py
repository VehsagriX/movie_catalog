import logging

from fastapi import Request, FastAPI

from app_lifespan import lifespan
from core import config
from api import router as api_router
from api.redirect_api_views import router as redirect_api_router


logging.basicConfig(
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
)

app = FastAPI(
    title="URL Shortener and Movie",
    lifespan=lifespan,
)
app.include_router(redirect_api_router)
app.include_router(api_router)


@app.get("/")
def read_root(request: Request, name: str = "World"):
    docs_url = request.url.replace(path="/docs", query="")
    return {
        "message": f"Hello {name}",
        "docs": docs_url,
    }
