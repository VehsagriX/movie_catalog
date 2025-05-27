from typing import Annotated

from fastapi import Header, HTTPException, status, Request

from core.config import API_TOKENS, UNSAFE_METHODS


def api_token_required(
    request: Request,
    api_token: Annotated[str, Header(alias="x-auth-token")] = "",
):
    if request.method not in UNSAFE_METHODS:
        return
    if api_token not in API_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token",
        )
