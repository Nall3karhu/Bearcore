from datetime import datetime



def create_action(
    action,
    target=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "action":
            action,

        "target":
            target,

        "status":
            "ready"

    }



def move(
    target
):

    return create_action(
        "move",
        target
    )



def grab(
    object_name
):

    return create_action(
        "grab",
        object_name
    )



def release(
    object_name
):

    return create_action(
        "release",
        object_name
    )



def status():

    return {

        "online": True,

        "mode":
            "standby"

    }