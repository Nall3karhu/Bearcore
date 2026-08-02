from datetime import datetime

from modules.knowledge_search.search import search_all
from modules.knowledge_graph.graph import find_node



def create_response(
    success,
    message,
    data=None
):

    return {

        "success":
            success,

        "time":
            datetime.now().isoformat(),

        "message":
            message,

        "data":
            data

    }



def search_knowledge(
    query
):

    results = search_all(
        query
    )


    return results



def check_graph(
    query
):

    results = find_node(
        query
    )


    return results



def process_query(
    query
):

    if not query:

        return create_response(

            False,

            "Tyhjä hakukysely"

        )



    search_results = search_knowledge(
        query
    )


    graph_results = check_graph(
        query
    )


    return create_response(

        True,

        "Tietohaku käsitelty",

        {

            "query":
                query,

            "search":
                search_results,

            "graph":
                graph_results

        }

    )



def add_knowledge_result(
    data,
    source
):

    return {

        "source":
            source,

        "data":
            data,

        "status":
            "stored",

        "time":
            datetime.now().isoformat()

    }



def controller_status():

    return {

        "controller":
            "online",

        "status":
            "ready"

    }