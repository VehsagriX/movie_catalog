from typing import Annotated

from fastapi import Query, HTTPException, status, Request

from core.config import API_TOKENS, UNSAFE_METHODS


def api_token_required(
    api_token: Annotated[str, Query()],
    request: Request,
):
    if request.method in UNSAFE_METHODS:
        if api_token not in API_TOKENS:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid API token",
            )
