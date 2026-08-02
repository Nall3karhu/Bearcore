from datetime import datetime



def create_status(
    name,
    value
):

    return {

        "time":
            datetime.now().isoformat(),

        "name":
            name,

        "value":
            value

    }



def get_system():

    return create_status(

        "system",

        "online"

    )



def get_temperature():

    return create_status(

        "temperature",

        None

    )



def get_devices():

    return create_status(

        "devices",

        []

    )



def control_device(
    device,
    command
):

    return {

        "success": True,

        "device":
            device,

        "command":
            command

    }