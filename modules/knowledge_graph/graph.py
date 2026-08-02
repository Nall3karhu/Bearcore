from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def graph_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "knowledge_graph"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "graph.json"
    )



def load_graph():

    file = graph_file()


    if not file or not file.exists():

        return {

            "nodes": [],

            "relations": []

        }


    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return {

            "nodes": [],

            "relations": []

        }



def save_graph(
    graph
):

    file = graph_file()


    if not file:

        return False


    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            graph,

            f,

            indent=4,

            ensure_ascii=False

        )


    return True



def add_node(
    name,
    category="general",
    data=None
):

    graph = load_graph()


    node = {

        "name":
            name,

        "category":
            category,

        "data":
            data,

        "created":
            datetime.now().isoformat()

    }


    graph["nodes"].append(
        node
    )


    save_graph(
        graph
    )


    return node



def add_relation(
    source,
    relation,
    target
):

    graph = load_graph()


    link = {

        "source":
            source,

        "relation":
            relation,

        "target":
            target,

        "created":
            datetime.now().isoformat()

    }


    graph["relations"].append(
        link
    )


    save_graph(
        graph
    )


    return link



def find_node(
    name
):

    graph = load_graph()


    results = []


    for node in graph["nodes"]:

        if node["name"].lower() == name.lower():

            results.append(
                node
            )


    return results



def get_connections(
    name
):

    graph = load_graph()


    results = []


    for relation in graph["relations"]:

        if (
            relation["source"] == name
            or
            relation["target"] == name
        ):

            results.append(
                relation
            )


    return results



def graph_status():

    graph = load_graph()


    return {

        "nodes":
            len(
                graph["nodes"]
            ),

        "relations":
            len(
                graph["relations"]
            ),

        "status":
            "online"

    }