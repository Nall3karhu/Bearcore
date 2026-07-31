import sqlite3
import config


def save_memory(key, value):
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    # Tarkistetaan onko avain jo olemassa
    cursor.execute(
        "SELECT id FROM memory WHERE key = ?",
        (key,)
    )

    result = cursor.fetchone()

    if result:
        # Päivitetään vanha tieto
        cursor.execute(
            "UPDATE memory SET value = ? WHERE key = ?",
            (value, key)
        )
        print("🔄 Muisti päivitetty!")
    else:
        # Lisätään uusi tieto
        cursor.execute(
            "INSERT INTO memory (key, value) VALUES (?, ?)",
            (key, value)
        )
        print("✅ Uusi muisti tallennettu!")

    connection.commit()
    connection.close()


def load_memory(key):
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT value FROM memory WHERE key = ?",
        (key,)
    )

    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]
    return None


def list_memories():
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT key, value FROM memory")

    memories = cursor.fetchall()

    connection.close()

    return memories