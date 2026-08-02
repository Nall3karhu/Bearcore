from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def update_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "updates"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "history.json"
    )



def load_history():

    file = update_file()


    if not file or not file.exists():

        return []


    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return []



def save_history(
    data
):

    file = update_file()


    if not file:

        return False


    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            data,

            f,

            indent=4,

            ensure_ascii=False

        )


    return True



def create_update(
    module,
    old_version,
    new_version
):

    return {

        "time":
            datetime.now().isoformat(),

        "module":
            module,

        "old_version":
            old_version,

        "new_version":
            new_version,

        "status":
            "planned"

    }



def check_update(
    module,
    current_version,
    latest_version
):

    if current_version != latest_version:

        return {

            "update":
                True,

            "module":
                module,

            "current":
                current_version,

            "latest":
                latest_version

        }


    return {

        "update":
            False,

        "module":
            module,

        "version":
            current_version

    }



def add_update(
    module,
    old_version,
    new_version
):

    history = load_history()


    history.append(

        create_update(

            module,

            old_version,

            new_version

        )

    )


    save_history(
        history
    )


    return True



def get_updates():

    return load_history()



def update_status():

    return {

        "manager":
            "online",

        "updates":
            len(
                load_history()
            )

    }