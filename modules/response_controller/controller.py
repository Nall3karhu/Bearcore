from datetime import datetime



def create_response(
    success,
    message,
    data=None,
    response_type="text"
):

    return {

        "success":
            success,

        "time":
            datetime.now().isoformat(),

        "type":
            response_type,

        "message":
            message,

        "data":
            data

    }



def from_assistant(
    assistant_result
):

    if not assistant_result:

        return create_response(

            False,

            "Tyhjä vastaus"

        )



    return create_response(

        assistant_result.get(
            "success",
            False
        ),

        assistant_result.get(
            "message",
            ""
        ),

        assistant_result.get(
            "data"
        )

    )



def format_text(
    response
):

    if response["success"]:

        return (

            "🐻 "

            +

            response["message"]

        )


    return (

        "❌ "

        +

        response["message"]

    )



def send_to_console(
    response
):

    return format_text(
        response
    )



def send_to_ui(
    response
):

    return {

        "display":
            response["message"],

        "status":
            response["success"]

    }



def send_to_voice(
    response
):

    return {

        "speak":
            response["message"]

    }



def controller_status():

    return {

        "controller":
            "online",

        "status":
            "ready"

    }