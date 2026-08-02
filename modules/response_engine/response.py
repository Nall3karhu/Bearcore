from datetime import datetime



def create_response(
    message,
    response_type="text",
    success=True,
    data=None
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



def success(
    message,
    data=None
):

    return create_response(

        message,

        "success",

        True,

        data

    )



def error(
    message
):

    return create_response(

        message,

        "error",

        False

    )



def info(
    message,
    data=None
):

    return create_response(

        message,

        "info",

        True,

        data

    )



def voice_response(
    text
):

    return create_response(

        text,

        "voice",

        True

    )



def studio_response(
    title,
    content
):

    return create_response(

        title,

        "studio",

        True,

        content

    )



def log_response(
    action,
    result
):

    return {

        "time":
            datetime.now().isoformat(),

        "action":
            action,

        "result":
            result

    }