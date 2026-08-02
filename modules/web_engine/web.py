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



def search(
    query
):

    if not query:

        return create_response(
            False,
            "Hakusana puuttuu"
        )


    return create_response(

        True,

        "🌐 Haku valmis",

        {

            "query":
                query,

            "results":
                []

        }

    )



def fetch(
    url
):

    return create_response(

        True,

        "📥 Sivun haku valmis",

        {

            "url":
                url

        }

    )



def analyze_result(
    result
):

    return create_response(

        True,

        "🧠 Tuloksen analysointi valmis",

        result

    )



def save_result(
    result
):

    return create_response(

        True,

        "💾 Tallennus valmis",

        result

    )