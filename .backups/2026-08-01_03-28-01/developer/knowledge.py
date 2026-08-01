import os
import json


HISTORY_FILE = "data/developer_history.json"



def module_info(args=None):

    if not args:

        print("❌ Käyttö: developer info <moduuli>")
        return


    name = args[-1]


    print("\n🐻 BearCore Knowledge")
    print("=" * 35)


    if not os.path.exists(HISTORY_FILE):

        print("❌ Ei rakennushistoriaa.")
        return



    with open(
        HISTORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        history = json.load(f)



    found = False


    for item in history:

        if item.get("module") == name:

            found = True

            print(f"\nModuuli: {name}")
            print(
                f"Tila: {item.get('status')}"
            )

            print(
                f"Luotu: {item.get('time')}"
            )


            path = os.path.join(
                "modules",
                name
            )


            print("\nTiedostot:")


            if os.path.exists(path):

                for file in os.listdir(path):

                    print(
                        f"✅ {file}"
                    )

            break



    if not found:

        print(
            "❌ Moduulia ei löydy muistista."
        )