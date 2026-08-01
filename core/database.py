import sqlite3
from pathlib import Path

import config
from core.logger import logger


def init_database():
    print(f"DATABASE = {config.DATABASE}")

    # Luodaan database-kansio tarvittaessa
    Path(config.DATABASE).parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(str(config.DATABASE))
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT,
            value TEXT
        )
    """)

    connection.commit()
    connection.close()

    logger.info("Tietokanta alustettu")