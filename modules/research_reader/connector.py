from datetime import datetime


from modules.web_research.reader import (
    read_page
)


from modules.research_analyzer.analyzer import (
    analyze_results
)



def collect_page_data(
    results
):

    pages = []


    for item in results:

        url = item.get(
            "link"
        )


        if not url:

            continue


        page = read_page(
            url
        )


        pages.append(

            {

                "title":
                    item.get(
                        "title"
                    ),

                "url":
                    url,

                "reader":
                    page

            }

        )


    return pages



def analyze_research_sources(
    topic,
    results
):

    pages = collect_page_data(
        results
    )


    analyzer_input = []


    for page in pages:

        analyzer_input.append(

            {

                "title":
                    page["title"]

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

        "pages":
            pages,

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