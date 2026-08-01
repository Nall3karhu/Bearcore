import json
import os
from datetime import datetime


MEMORY_FILE = "improvement_memory.json"


def improvement_memory(args=None):

    print("🐻 Improvement Memory käynnissä")

    if not args:
        print("ℹ️ Ei tietoa käsiteltäväksi")
        return True

    data = []

    if os.path.exists(MEMORY_FILE):

        try:
            with open(
                MEMORY_FILE,
                "r",
                encoding="utf-8"
            ) as f:
                data = json.load(f)

        except Exception:
            data = []


    action = args[0]


    # Haku
    if action == "search":

        if len(args) < 2:
            return False

        query = args[1]

        print(
            f"🔎 Haetaan muistista: {query}"
        )

        found = False

        for item in data:

            if query.lower() in item.get(
                "error",
                ""
            ).lower():

                print("✅ Löytyi:")
                print(
                    "Virhe:",
                    item.get("error")
                )

                print(
                    "Ratkaisu:",
                    item.get("solution")
                )

                found = True

        return found


    # Tallennus
    if action == "save":

        if len(args) < 3:
            return False


        entry = {

            "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "error":
                args[1],

            "solution":
                args[2]
        }


        data.append(entry)


        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


        print(
            "✅ Ratkaisu tallennettu muistiin"
        )

        return True


    return False