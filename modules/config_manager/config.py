from pathlib import Path
from datetime import datetime
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def config_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "config"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "settings.json"
    )



def default_config():

    return {

        "name":
            "BearCore",

        "version":
            "0.1",

        "mode":
            "development",

        "created":
            datetime.now().isoformat(),

        "settings":

            {

                "auto_start":
                    False,

                "logging":
                    True,

                "learning":
                    True

            }

    }



def load_config():

    file = config_file()


    if not file:

        return default_config()



    if not file.exists():

        save_config(
            default_config()
        )


    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return default_config()



def save_config(
    data
):

    file = config_file()


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



def get_setting(
    key
):

    config = load_config()


    return (

        config
        .get(
            "settings",
            {}
        )
        .get(
            key
        )

    )



def set_setting(
    key,
    value
):

    config = load_config()


    config["settings"][key] = value


    save_config(
        config
    )


    return True



def config_status():

    return {

        "name":
            "BearCore",

        "status":
            "ready",

        "version":
            load_config()
            .get(
                "version"
            )

    }