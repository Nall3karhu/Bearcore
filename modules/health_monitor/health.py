from pathlib import Path
import datetime



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def check_modules():

    base = find_bearcore()

    if not base:

        return False


    modules = base / "modules"


    if modules.exists():

        return True


    return False



def check_memory():

    base = find_bearcore()

    if not base:

        return False


    return (
        base /
        "memory"
    ).exists()



def check_knowledge():

    base = find_bearcore()

    if not base:

        return False


    return (
        base /
        "knowledge"
    ).exists()



def check_system():

    return {

        "time":
            datetime.datetime.now().isoformat(),

        "modules":
            check_modules(),

        "memory":
            check_memory(),

        "knowledge":
            check_knowledge(),

        "status":
            "online"

    }



def health():

    data = check_system()


    return {

        "success":
            True,

        "health":
            data

    }