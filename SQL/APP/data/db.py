import sqlite3
from pathlib import Path

# Always build paths relative to PROJECT ROOT
BASE_DIR = Path(__file__).resolve().parents[3]   # Coursework2Project
DATA_DIR = BASE_DIR / "DATA"
DB_PATH = DATA_DIR / "intelligence_platform.db"


def connect_database(db_path=DB_PATH):
    """Connect to SQLite database."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)  # ensure DATA exists
    return sqlite3.connect(str(db_path))
