from pathlib import Path
from datetime import datetime
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def knowledge_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "knowledge"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "knowledge.json"
    )



def create_entry(
    title,
    content,
    source=None,
    category="general"
):

    return {

        "time":
            datetime.now().isoformat(),

        "title":
            title,

        "content":
            content,

        "source":
            source,

        "category":
            category

    }



def save_knowledge(
    title,
    content,
    source=None,
    category="general"
):

    file = knowledge_file()


    if not file:

        return False



    data = []


    if file.exists():

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)


        except:

            data = []



    data.append(
        create_entry(
            title,
            content,
            source,
            category
        )
    )



    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


    return True



def get_knowledge(
    limit=50
):

    file = knowledge_file()


    if not file or not file.exists():

        return []



    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        return data[-limit:]


    except:

        return []



def search_knowledge(
    keyword
):

    data = get_knowledge(
        10000
    )


    results = []


    for item in data:

        text = (
            str(
                item.get(
                    "title",
                    ""
                )
            )
            +
            " "
            +
            str(
                item.get(
                    "content",
                    ""
                )
            )
        )


        if keyword.lower() in text.lower():

            results.append(
                item
            )


    return results



def add_source(
    title,
    url
):

    return save_knowledge(

        title,

        f"Lähde: {url}",

        url,

        "source"

    )



def clear_knowledge():

    file = knowledge_file()


    if file and file.exists():

        file.unlink()


    return True