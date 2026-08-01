import os
import json
from datetime import datetime


HISTORY_FILE = "data/developer_history.json"


def save_history(module, status):

    os.makedirs("data", exist_ok=True)

    history = []

    if os.path.exists(HISTORY_FILE):

        try:

            with open(
                HISTORY_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                history = json.load(f)

        except:

            history = []


    history.append(
        {
            "module": module,
            "status": status,
            "time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }
    )


    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            history,
            f,
            indent=4,
            ensure_ascii=False
        )



def show_history(args=None):

    print("\n🐻 BearCore Development History")
    print("=" * 40)


    if not os.path.exists(HISTORY_FILE):

        print("Ei rakennushistoriaa vielä.")

        return


    with open(
        HISTORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        history = json.load(f)


    if len(history) == 0:

        print("Ei rakennushistoriaa vielä.")

        return


    for item in history:

        print("\n✅ Moduuli:")
        print(
            f"   {item['module']}"
        )

        print(
            f"   Tila: {item['status']}"
        )

        print(
            f"   Aika: {item['time']}"
        )


    print(
        f"\nRakennettu moduuleita: {len(history)}"
    )