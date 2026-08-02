from datetime import datetime



def response(
    success,
    message,
    data=None
):

    return {

        "success": success,

        "time":
            datetime.now().isoformat(),

        "message":
            message,

        "data":
            data

    }



def request(
    endpoint,
    data=None
):

    return response(

        True,

        "🔌 API request vastaanotettu",

        {
            "endpoint": endpoint,
            "data": data
        }

    )



def register_endpoint(
    name
):

    return response(

        True,

        "✅ Endpoint rekisteröity",

        name

    )



def api_status():

    return response(

        True,

        "🌐 API online"

    )