from datetime import datetime



def create_result(
    query,
    content=None,
    source=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "query":
            query,

        "content":
            content,

        "source":
            source

    }



def search(
    query
):

    if not query:

        return {

            "success": False,

            "message":
                "Hakusana puuttuu"

        }



    return {

        "success": True,

        "result":
            create_result(

                query,

                "Hakutuloksen pohja",

                None

            )

    }



def save_result(
    result
):

    return {

        "success": True,

        "message":
            "🌐 Tulos tallennettu"

    }