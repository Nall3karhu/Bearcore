from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def create_response(
    name,
    value,
    status=True
):

    return {

        "success": status,

        "name": name,

        "value": value

    }



def get_modules():

    base = find_bearcore()

    if not base:

        return create_response(
            "modules",
            0,
            False
        )


    modules_dir = (
        base /
        "modules"
    )


    count = 0


    if modules_dir.exists():

        for item in modules_dir.iterdir():

            if item.is_dir():

                count += 1



    return create_response(
        "modules",
        count
    )



def get_reports():

    base = find_bearcore()

    if not base:

        return create_response(
            "reports",
            0,
            False
        )


    reports = (
        base /
        "reports"
    )


    count = 0


    if reports.exists():

        count = len(
            list(
                reports.glob("*.json")
            )
        )


    return create_response(
        "reports",
        count
    )



def get_backups():

    base = find_bearcore()

    if not base:

        return create_response(
            "backups",
            0,
            False
        )


    backups = (
        base /
        "backups"
    )


    count = 0


    if backups.exists():

        count = len(
            list(
                backups.glob("*")
            )
        )


    return create_response(
        "backups",
        count
    )



def get_status():

    return create_response(
        "status",
        "ONLINE"
    )



def get_dashboard():

    return {

        "modules":
            get_modules(),

        "reports":
            get_reports(),

        "backups":
            get_backups(),

        "status":
            get_status()

    }