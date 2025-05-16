from fastapi import Request, FastAPI

from api import router as api_router
from api.redirect_api_views import router as redirect_api_router


app = FastAPI()
app.include_router(redirect_api_router)
app.include_router(api_router)


@app.get("/")
def read_root(request: Request, name: str = "World"):
    docs_url = request.url.replace(path="/docs", query="")
    return {
        "message": f"Hello {name}",
        "docs": docs_url,
    }
