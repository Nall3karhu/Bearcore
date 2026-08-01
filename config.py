from pathlib import Path

# BearCore asetukset

BASE_DIR = Path(__file__).resolve().parent

APP_NAME = "BearCore"
VERSION = "0.2"

DATABASE = BASE_DIR / "database" / "bearcore.db"

MEMORY_FOLDER = BASE_DIR / "memory"

LOG_FOLDER = BASE_DIR / "data" / "logs"

DEBUG = True