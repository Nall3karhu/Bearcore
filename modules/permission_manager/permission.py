from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def permission_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "permissions"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "permissions.json"
    )



def load_permissions():

    file = permission_file()


    if not file or not file.exists():

        return {

            "allowed": [],

            "blocked": []

        }


    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return {

            "allowed": [],

            "blocked": []

        }



def save_permissions(
    data
):

    file = permission_file()


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



def add_permission(
    action
):

    permissions = load_permissions()


    if action not in permissions["allowed"]:

        permissions["allowed"].append(
            action
        )


    save_permissions(
        permissions
    )


    return True



def block_permission(
    action
):

    permissions = load_permissions()


    if action not in permissions["blocked"]:

        permissions["blocked"].append(
            action
        )


    save_permissions(
        permissions
    )


    return True



def check_permission(
    action
):

    permissions = load_permissions()


    if action in permissions["blocked"]:

        return {

            "allowed":
                False,

            "reason":
                "blocked"

        }



    if action in permissions["allowed"]:

        return {

            "allowed":
                True,

            "reason":
                "approved"

        }



    return {

        "allowed":
            False,

        "reason":
            "confirmation_required"

    }



def request_permission(
    action
):

    return {

        "action":
            action,

        "status":
            "waiting_confirmation",

        "time":
            datetime.now().isoformat()

    }



def permission_status():

    permissions = load_permissions()


    return {

        "manager":
            "online",

        "allowed":
            len(
                permissions["allowed"]
            ),

        "blocked":
            len(
                permissions["blocked"]
            )

    }