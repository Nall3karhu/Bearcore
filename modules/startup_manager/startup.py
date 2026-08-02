from datetime import datetime



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



def check_component(
    name
):

    return {

        "name":
            name,

        "status":
            "ready"

    }



def load_kernel():

    return check_component(
        "Kernel"
    )



def load_modules():

    return check_component(
        "Modules"
    )



def load_controllers():

    return check_component(
        "Controllers"
    )



def load_health():

    return check_component(
        "Health"
    )



def startup():

    components = [

        load_kernel(),

        load_modules(),

        load_controllers(),

        load_health()

    ]


    return create_response(

        True,

        "🐻 BearCore käynnistetty",

        {

            "components":
                components,

            "status":
                "online"

        }

    )



def shutdown():

    return create_response(

        True,

        "🐻 BearCore suljettu"

    )



def restart():

    return create_response(

        True,

        "🔄 BearCore uudelleenkäynnistys valmis"

    )