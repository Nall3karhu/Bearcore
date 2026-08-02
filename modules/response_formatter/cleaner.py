from datetime import datetime



def clean_research_response(
    result
):

    data = result.get(
        "data",
        {}
    )


    research = data.get(
        "research",
        {}
    )


    summary = research.get(
        "summary",
        {}
    )


    analysis = research.get(
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
        "🔎 Tutkimus valmis"
    )


    lines.append(
        ""
    )


    lines.append(
        "Aihe:"
    )


    lines.append(

        research.get(
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
        "Keskeiset tiedot:"
    )


    for item in summary.get(
        "summaries",
        []
    ):

        title = item.get(
            "title",
            ""
        )


        text = item.get(
            "summary",
            ""
        )


        if title:

            lines.append(

                f"- {title}"

            )


        if text:

            lines.append(

                text[:200]

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