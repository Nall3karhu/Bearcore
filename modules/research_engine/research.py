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



def research(
    topic
):

    if not topic:

        return create_response(
            False,
            "Aihe puuttuu"
        )


    return create_response(

        True,

        "🔎 Tutkimus valmis",

        {

            "topic":
                topic,

            "sources":
                [],

            "summary":
                None

        }

    )



def add_source(
    research_data,
    source
):

    research_data["sources"].append(
        source
    )


    return research_data



def create_summary(
    research_data
):

    research_data["summary"] = (
        "Yhteenveto valmis"
    )


    return research_data