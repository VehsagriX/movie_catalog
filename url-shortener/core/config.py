import logging
from pathlib import Path


# Конфиг Хранения данных в json
BASE_DIR = Path(__file__).resolve().parent.parent
SHORT_URL_STORAGE_FILE = BASE_DIR / "Short-URLS.json"
MOVIE_STORAGE_FILE = BASE_DIR / "Movies.json"

# Конфиг ЛОГИРОВАНИЯ
LOG_FORMAT = "%(asctime)s %(name)-12s %(levelname)-8s  %(funcName)s %(message)s"
LOG_LEVEL = logging.INFO
