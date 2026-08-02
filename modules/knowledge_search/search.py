from datetime import datetime



def create_result(
    keyword,
    results=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "keyword":
            keyword,

        "results":
            results or [],

        "count":
            len(
                results or []
            )

    }



def search_memory(
    keyword,
    memory=None
):

    if not memory:

        return []


    results = []


    for item in memory:

        text = str(
            item
        )


        if keyword.lower() in text.lower():

            results.append(
                item
            )


    return results



def search_knowledge(
    keyword,
    knowledge=None
):

    if not knowledge:

        return []


    results = []


    for item in knowledge:

        text = str(
            item
        )


        if keyword.lower() in text.lower():

            results.append(
                item
            )


    return results



def search_all(
    keyword,
    memory=None,
    knowledge=None
):

    memory_results = search_memory(

        keyword,

        memory

    )


    knowledge_results = search_knowledge(

        keyword,

        knowledge

    )


    return create_result(

        keyword,

        memory_results +
        knowledge_results

    )



def add_external_result(
    result,
    source
):

    return {

        "source":
            source,

        "result":
            result,

        "added":
            datetime.now().isoformat()

    }



def status():

    return {

        "controller":
            "online",

        "mode":
            "search"

    }