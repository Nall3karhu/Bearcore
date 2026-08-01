import os
import shutil
import json
from datetime import datetime


PLUGIN_PATH = "modules/developer/commands"

BACKUP_PATH = "data/plugin_backups"



def backup_plugin(args=None):

    if not args:

        print(
            "❌ Käyttö: developer backup plugin <nimi>"
        )

        return


    name = args[-1]


    source = os.path.join(
        PLUGIN_PATH,
        f"{name}.py"
    )


    if not os.path.exists(source):

        print(
            "❌ Pluginia ei löytynyt."
        )

        return


    destination = os.path.join(
        BACKUP_PATH,
        name
    )


    os.makedirs(
        destination,
        exist_ok=True
    )


    shutil.copy(
        source,
        destination
    )


    info = {

        "plugin": name,

        "backup_time":
            str(datetime.now()),

        "status":
            "backup created"

    }


    with open(
        os.path.join(
            destination,
            "info.json"
        ),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            info,
            f,
            indent=4
        )


    print(
        f"💾 Varmuuskopio luotu: {name}"
    )



def restore_plugin(args=None):

    if not args:

        print(
            "❌ Käyttö: developer restore plugin <nimi>"
        )

        return


    name = args[-1]


    backup = os.path.join(
        BACKUP_PATH,
        name,
        f"{name}.py"
    )


    if not os.path.exists(backup):

        print(
            "❌ Varmuuskopiota ei löytynyt."
        )

        return


    shutil.copy(
        backup,
        PLUGIN_PATH
    )


    print(
        f"♻️ Palautettu plugin: {name}"
    )