from datetime import datetime



def analyze_results(
    topic,
    results
):

    sources = []


    for item in results:

        if item.get("title"):

            sources.append(
                item["title"]
            )


    return {

        "success":
            True,

        "time":
            datetime.now().isoformat(),

        "topic":
            topic,

        "source_count":
            len(results),

        "sources":
            sources,

        "summary":

            f"Tutkimus aiheesta '{topic}' analysoitu. Löytyi {len(results)} lähdettä."

    }



def format_analysis(
    analysis
):

    lines = []


    lines.append(
        "🐻 BearCore:"
    )

    lines.append(
        ""
    )

    lines.append(
        "🔎 Tutkimusanalyysi valmis"
    )

    lines.append(
        ""
    )

    lines.append(
        f"Aihe:\n{analysis['topic']}"
    )

    lines.append(
        ""
    )

    lines.append(
        "Lähteitä:"
    )


    for source in analysis["sources"]:

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
        analysis["summary"]
    )


    return "\n".join(
        lines
    )



def analyzer_status():

    return {

        "module":
            "research_analyzer",

        "status":
            "ready"

    }