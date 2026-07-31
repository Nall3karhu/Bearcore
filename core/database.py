import sqlite3
import config
from core.logger import logger


def init_database():
    connection = sqlite3.connect(config.DATABASE)
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