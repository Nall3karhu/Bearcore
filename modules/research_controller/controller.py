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



def start_research(
    topic
):

    if not topic:

        return response(
            False,
            "Tutkimusaihe puuttuu"
        )


    research = {

        "topic":
            topic,

        "sources":
            [],

        "knowledge":
            None,

        "report":
            None

    }


    return response(

        True,

        "🔎 Tutkimus käynnistetty",

        research

    )



def add_result(
    research,
    result
):

    research["sources"].append(
        result
    )


    return research



def finish_research(
    research
):

    research["knowledge"] = (
        "Tieto käsitelty"
    )

    research["report"] = (
        "Raportti valmis"
    )


    return response(

        True,

        "✅ Tutkimus valmis",

        research

    )