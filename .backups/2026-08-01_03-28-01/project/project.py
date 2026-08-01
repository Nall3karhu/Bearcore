import config
import os
import sqlite3


def project(args=None):

    print("\n==============================")
    print("🐻 BearCore Project Status")
    print("==============================")

    print(f"Versio: {config.VERSION}")

    # Tietokanta
    try:
        sqlite3.connect(config.DATABASE).close()
        print("Tietokanta: ✅ OK")
    except:
        print("Tietokanta: ❌ Virhe")

    # Muistien määrä
    try:
        conn = sqlite3.connect(config.DATABASE)
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM memory")

        amount = cur.fetchone()[0]

        conn.close()

        print(f"Muistit: {amount}")

    except:
        print("Muistit: Ei saatavilla")

    # Moduulit
    print("\nLöydetyt moduulit:")

    if os.path.exists("modules"):

        for folder in sorted(os.listdir("modules")):

            if os.path.isdir(os.path.join("modules", folder)):
                print(f"✅ {folder}")

    print("\nBearCore toimii normaalisti.")