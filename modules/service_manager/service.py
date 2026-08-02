from pathlib import Path
from datetime import datetime



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def create_response(
    success,
    message,
    data=None
):

    return {

        "success":
            success,

        "time":
            datetime.now().isoformat(),

        "message":
            message,

        "data":
            data

    }



def get_modules():

    base = find_bearcore()


    if not base:

        return []



    modules_path = (
        base /
        "modules"
    )


    if not modules_path.exists():

        return []



    modules = []


    for item in modules_path.iterdir():

        if item.is_dir():

            if item.name != "__pycache__":

                modules.append(
                    item.name
                )


    return modules



def check_module(
    name
):

    modules = get_modules()


    return {

        "name":
            name,

        "loaded":
            name in modules,

        "status":
            "ready"

            if name in modules

            else

            "missing"

    }



def load_module(
    name
):

    result = check_module(
        name
    )


    if result["loaded"]:

        return create_response(

            True,

            "✅ Moduuli ladattu",

            result

        )


    return create_response(

        False,

        "❌ Moduulia ei löytynyt",

        result

    )



def load_all():

    modules = get_modules()


    loaded = []


    for module in modules:

        loaded.append(

            check_module(
                module
            )

        )


    return create_response(

        True,

        "🐻 Moduulit tarkistettu",

        loaded

    )



def service_status():

    return {

        "manager":
            "online",

        "modules":
            len(
                get_modules()
            ),

        "status":
            "ready"

    }