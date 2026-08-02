from datetime import datetime



def clean_research_response(
    result
):

    data = result.get(
        "data",
        {}
    )


    analysis = data.get(
        "analysis",
        {}
    )


    lines = []


    lines.append(
        "🐻 BearCore:"
    )


    lines.append(
        ""
    )


    lines.append(
        "🔎 Löysin tietoa aiheesta:"
    )


    lines.append(
        analysis.get(
            "topic",
            "Tuntematon"
        )
    )


    lines.append(
        ""
    )


    lines.append(
        "Lähteet:"
    )


    for source in analysis.get(
        "sources",
        []
    ):

        lines.append(
            f"✅ {source}"
        )


    lines.append(
        ""
    )


    lines.append(
        "Yhteenveto:"
    )


    lines.append(
        analysis.get(
            "summary",
            ""
        )
    )


    lines.append(
        ""
    )


    lines.append(
        "Tallennettu:"
    )


    lines.append(
        "✅ Knowledge"
    )


    lines.append(
        "✅ Learning"
    )


    return "\n".join(
        lines
    )



def formatter_status():

    return {

        "module":
            "response_formatter",

        "status":
            "ready"

    }