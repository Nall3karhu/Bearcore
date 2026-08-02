from pathlib import Path
from datetime import datetime
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def registry_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "registry"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "modules.json"
    )



def load_registry():

    file = registry_file()


    if not file:

        return []



    if not file.exists():

        save_registry([])



    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return []



def save_registry(
    data
):

    file = registry_file()


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



def register_module(
    name,
    version="1.0",
    status="ready"
):

    registry = load_registry()


    item = {

        "name":
            name,

        "version":
            version,

        "status":
            status,

        "registered":
            datetime.now().isoformat()

    }


    registry.append(
        item
    )


    save_registry(
        registry
    )


    return item



def list_modules():

    return load_registry()



def find_module(
    name
):

    modules = load_registry()


    for module in modules:

        if module["name"] == name:

            return module


    return None



def update_status(
    name,
    status
):

    modules = load_registry()


    for module in modules:

        if module["name"] == name:

            module["status"] = status


    save_registry(
        modules
    )


    return True



def registry_status():

    return {

        "modules":
            len(
                load_registry()
            ),

        "status":
            "online"

    }