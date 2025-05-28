import logging
from pathlib import Path


# Конфиг Хранения данных в json
BASE_DIR = Path(__file__).resolve().parent.parent
SHORT_URL_STORAGE_FILE = BASE_DIR / "Short-URLS.json"
MOVIE_STORAGE_FILE = BASE_DIR / "Movies.json"

# Конфиг ЛОГИРОВАНИЯ
LOG_FORMAT = (
    "[%(asctime)-2s] File: %(name)-12s %(levelname)-8s:  %(funcName)s - %(message)s"
)
LOG_LEVEL = logging.INFO


UNSAFE_METHODS = frozenset(
    {
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    }
)

API_TOKENS: frozenset[str] = frozenset(
    {
        "IexqJ9E4DNswYEv1GMtkMg",
        "2d6Y1bfx3lUj4cRWwjBDHOSgbXk",
    }
)


USERS_DB: dict[str, str] = {
    # username: password
    "sam": "password",
    "bob": "qwerty",
}
