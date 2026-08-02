from datetime import datetime



def create_response(
    success,
    command,
    target,
    data=None
):

    return {

        "success":
            success,

        "time":
            datetime.now().isoformat(),

        "command":
            command,

        "target":
            target,

        "data":
            data

    }



def find_target(
    command
):

    command = command.lower().strip()



    routes = {

        "status":
            "health",

        "health":
            "health",

        "test":
            "self_test",

        "backup":
            "backup",

        "modules":
            "registry",

        "update":
            "update"

    }



    return routes.get(
        command,
        "assistant"
    )



def route(
    command
):

    if not command:

        return create_response(

            False,

            command,

            None,

            "Tyhjä komento"

        )



    target = find_target(
        command
    )


    return create_response(

        True,

        command,

        target

    )



def router_status():

    return {

        "router":
            "online",

        "status":
            "ready"

    }