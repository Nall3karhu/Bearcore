from datetime import datetime



def format_response(
    response
):

    if response is None:

        return "❌ Ei vastausta"



    if isinstance(response, str):

        return response



    if not isinstance(response, dict):

        return str(response)



    lines = []


    message = response.get(
        "message"
    )


    if message:

        lines.append(
            "🐻 BearCore:"
        )

        lines.append(
            message
        )



    data = response.get(
        "data"
    )


    if isinstance(data, dict):

        lines.append(
            ""
        )

        lines.append(
            "Tiedot:"
        )


        for key, value in data.items():

            lines.append(

                f"• {key}: {value}"

            )



    result = "\n".join(
        lines
    )


    if not result:

        result = str(
            response
        )


    return result



def formatter_status():

    return {

        "module":
            "response_formatter",

        "status":
            "ready",

        "time":
            datetime.now().isoformat()

    }