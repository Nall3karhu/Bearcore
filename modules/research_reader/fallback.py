from datetime import datetime



from modules.web_research.reader import (
    read_page
)



def read_with_fallback(
    results
):

    collected = []


    for item in results:

        title = item.get(
            "title",
            "Tuntematon"
        )

        url = item.get(
            "link"
        )


        if url:

            page = read_page(
                url
            )


            if page["success"]:

                collected.append(

                    {

                        "title":
                            title,

                        "url":
                            url,

                        "source":
                            "page",

                        "content":
                            page["content"]

                    }

                )


            else:

                collected.append(

                    {

                        "title":
                            title,

                        "url":
                            url,

                        "source":
                            "search_summary",

                        "content":
                            item.get(
                                "summary",
                                ""
                            )

                    }

                )


        else:

            collected.append(

                {

                    "title":
                        title,

                    "source":
                        "search_summary",

                    "content":
                        item.get(
                            "summary",
                            ""
                        )

                }

            )


    return {

        "success":
            True,

        "time":
            datetime.now().isoformat(),

        "pages":
            collected

    }



def fallback_status():

    return {

        "module":
            "reader_fallback",

        "status":
            "ready"

    }