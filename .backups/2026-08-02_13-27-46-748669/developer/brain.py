import os
import json


HISTORY_FILE = "data/developer_history.json"


def show_brain(args=None):

    print("\n🐻 BearCore Project Brain")
    print("=" * 40)


    modules_path = "modules"

    modules = []


    if os.path.exists(modules_path):

        for folder in os.listdir(modules_path):

            path = os.path.join(
                modules_path,
                folder
            )

            if os.path.isdir(path):

                if folder != "__pycache__":

                    modules.append(folder)



    print(f"\n📦 Moduuleita: {len(modules)}")


    print("\nModuulit:")

    for module in sorted(modules):

        print(f"✅ {module}")



    print("\n🧠 Rakennushistoria:")


    if os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            history = json.load(f)


        if history:

            for item in history[-5:]:

                print(
                    f"✅ {item['module']} - {item['status']}"
                )


            print(
                "\nViimeisin rakennus:"
            )

            print(
                history[-1]["module"]
            )


        else:

            print("Ei rakennuksia vielä.")


    else:

        print("Ei historiaa vielä.")



    print("\n🟢 Brain valmis.")