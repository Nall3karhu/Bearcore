from datetime import datetime



def create_plugin(
    name
):

    return {

        "name":
            name,

        "created":
            datetime.now().isoformat(),

        "status":
            "ready"

    }



def load_plugin(
    name
):

    return {

        "success":
            True,

        "plugin":
            name,

        "status":
            "loaded"

    }



def unload_plugin(
    name
):

    return {

        "success":
            True,

        "plugin":
            name,

        "status":
            "unloaded"

    }



def list_plugins():

    return []