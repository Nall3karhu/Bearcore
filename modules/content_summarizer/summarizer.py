from datetime import datetime



def summarize_content(
    topic,
    pages
):

    summaries = []


    for page in pages:

        content = page.get(
            "content",
            ""
        )


        if not content:

            continue


        summary = content[:500]


        summaries.append(

            {

                "title":
                    page.get(
                        "title",
                        "Tuntematon"
                    ),

                "summary":
                    summary

            }

        )


    return {

        "success":
            True,

        "time":
            datetime.now().isoformat(),

        "topic":
            topic,

        "sources":
            len(summaries),

        "summaries":
            summaries

    }



def format_summary(
    result
):

    lines = []


    lines.append(
        "🐻 BearCore:"
    )


    lines.append(
        ""
    )


    lines.append(
        "📚 Sisältöanalyysi valmis"
    )


    lines.append(
        ""
    )


    lines.append(
        f"Aihe:\n{result.get('topic')}"
    )


    lines.append(
        ""
    )


    for item in result.get(
        "summaries",
        []
    ):

        lines.append(
            "Lähde:"
        )


        lines.append(
            item["title"]
        )


        lines.append(
            item["summary"]
        )


        lines.append(
            ""
        )


    return "\n".join(
        lines
    )



def summarizer_status():

    return {

        "module":
            "content_summarizer",

        "status":
            "ready"

    }