from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SHORT_URL_STORAGE_FILE = BASE_DIR / "Short-URLS.json"
MOVIE_STORAGE_FILE = BASE_DIR / "Movies.json"
