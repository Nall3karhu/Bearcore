from datetime import datetime


from modules.research_reader.fallback import (
    read_with_fallback
)


from modules.content_summarizer.summarizer import (
    summarize_content
)


from modules.research_analyzer.analyzer import (
    analyze_results
)



def analyze_research_sources(
    topic,
    results
):


    read_result = read_with_fallback(
        results
    )


    pages = read_result.get(
        "pages",
        []
    )


    summaries = summarize_content(

        topic,

        pages

    )


    analyzer_input = []


    for item in summaries.get(
        "summaries",
        []
    ):

        analyzer_input.append(

            {

                "title":
                    item.get(
                        "title"
                    ),

                "summary":
                    item.get(
                        "summary"
                    )

            }

        )


    analysis = analyze_results(

        topic,

        analyzer_input

    )


    return {

        "success":
            True,

        "time":
            datetime.now().isoformat(),

        "topic":
            topic,

        "reader":
            read_result,

        "summary":
            summaries,

        "analysis":
            analysis

    }



def reader_connector_status():

    return {

        "module":
            "research_reader",

        "status":
            "ready"

    }