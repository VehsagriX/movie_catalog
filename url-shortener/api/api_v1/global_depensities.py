import logging
from typing import Annotated

from fastapi import HTTPException, status, Request, Depends
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
    HTTPBasic,
    HTTPBasicCredentials,
)
from core.config import API_TOKENS, UNSAFE_METHODS, USERS_DB

logger = logging.getLogger(__name__)


security = HTTPBearer(
    scheme_name="Static api token",
    description="YOUR **Static API token** from the developer portal.",
    auto_error=False,
)

user_basic_auth = HTTPBasic(
    scheme_name="Basic auth",
    description="Basic username  + password auth",
    auto_error=False,
)


def validate_api_token(api_token: HTTPAuthorizationCredentials):
    if api_token.credentials in API_TOKENS:
        return
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API token",
    )


def api_token_required(
    request: Request,
    api_token: Annotated[HTTPAuthorizationCredentials | None, Depends(security)] = None,
):
    logger.info("API token: %s", api_token)
    if request.method not in UNSAFE_METHODS:
        return

    if not api_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API token is required.",
        )
    validate_api_token(api_token=api_token)


def validate_basic_auth(
    credentials: HTTPBasicCredentials | None,
):
    if (
        credentials
        and credentials.username in USERS_DB
        and credentials.password == USERS_DB[credentials.username]
    ):
        return

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User credentials is required. Invalid username or password.",
        headers={"WWW-Authenticate": "Basic"},
    )


def user_basic_auth_required(
    request: Request,
    credentials: Annotated[
        HTTPBasicCredentials | None,
        Depends(user_basic_auth),
    ] = None,
):
    logger.info("User basic auth credentials: %s", credentials)

    if request.method not in UNSAFE_METHODS:
        return

    validate_basic_auth(credentials=credentials)


def api_token_or_user_basic_auth_required_for_unsafe_methods(
    request: Request,
    credentials: Annotated[
        HTTPBasicCredentials | None,
        Depends(user_basic_auth),
    ] = None,
    api_token: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(security),
    ] = None,
):
    if request.method not in UNSAFE_METHODS:
        return

    if credentials:
        return validate_basic_auth(credentials=credentials)

    if api_token:
        return validate_api_token(api_token=api_token)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="API token or basic auth is required.",
    )
