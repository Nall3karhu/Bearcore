from pathlib import Path
from datetime import datetime
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def profile_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "profile"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "user.json"
    )



def default_profile():

    return {

        "created":
            datetime.now().isoformat(),

        "settings":
            {},

        "preferences":
            {},

        "history":
            []

    }



def load_profile():

    file = profile_file()


    if not file:

        return default_profile()



    if not file.exists():

        save_profile(
            default_profile()
        )


    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return default_profile()



def save_profile(
    data
):

    file = profile_file()


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



def set_preference(
    key,
    value
):

    profile = load_profile()


    profile["preferences"][key] = value


    save_profile(
        profile
    )


    return True



def get_preference(
    key
):

    profile = load_profile()


    return profile["preferences"].get(
        key
    )



def set_setting(
    key,
    value
):

    profile = load_profile()


    profile["settings"][key] = value


    save_profile(
        profile
    )


    return True



def add_history(
    event
):

    profile = load_profile()


    profile["history"].append({

        "time":
            datetime.now().isoformat(),

        "event":
            event

    })


    save_profile(
        profile
    )


    return True



def get_profile():

    return load_profile()



def profile_status():

    profile = load_profile()


    return {

        "manager":
            "online",

        "preferences":
            len(
                profile["preferences"]
            ),

        "history":
            len(
                profile["history"]
            )

    }