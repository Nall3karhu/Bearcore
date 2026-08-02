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



def boot():

    return create_response(

        True,

        "🐻 BearCore Kernel käynnistetty",

        {

            "status":
                "online"

        }

    )



def shutdown():

    return create_response(

        True,

        "🐻 BearCore sammutettu"

    )



def status():

    return {

        "kernel":
            "online",

        "time":
            datetime.now().isoformat()

    }



def execute(
    command
):

    if not command:

        return create_response(

            False,

            "Tyhjä komento"

        )



    return create_response(

        True,

        "⚙️ Komento vastaanotettu",

        {

            "command":
                command

        }

    )