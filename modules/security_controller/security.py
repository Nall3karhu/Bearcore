from datetime import datetime



def create_response(
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



def check_permission(
    action
):

    return create_response(

        True,

        "✅ Toiminto sallittu",

        action

    )



def request_confirmation(
    action
):

    return create_response(

        True,

        "⏳ Vahvistus tarvitaan",

        action

    )



def store_secret(
    name,
    value
):

    return create_response(

        True,

        "🔐 Tieto tallennettu",

        {
            "name": name
        }

    )



def remove_secret(
    name
):

    return create_response(

        True,

        "🗑 Tieto poistettu",

        name

    )



def security_status():

    return create_response(

        True,

        "🛡 Security online"

    )