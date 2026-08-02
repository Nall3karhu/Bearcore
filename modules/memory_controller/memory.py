from pathlib import Path
from datetime import datetime
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def memory_file():

    base = find_bearcore()

    if not base:

        return None


    memory_dir = (
        base /
        "memory"
    )


    memory_dir.mkdir(
        exist_ok=True
    )


    return (
        memory_dir /
        "memory.json"
    )



def create_memory(
    category,
    content
):

    return {

        "time":
            datetime.now().isoformat(),

        "category":
            category,

        "content":
            content

    }



def save_memory(
    category,
    content
):

    file = memory_file()


    if not file:

        return False



    memories = []


    if file.exists():

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                memories = json.load(f)


        except:

            memories = []



    memories.append(
        create_memory(
            category,
            content
        )
    )



    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memories,
            f,
            indent=4,
            ensure_ascii=False
        )


    return True



def get_memory(
    limit=20
):

    file = memory_file()


    if not file or not file.exists():

        return []



    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            memories = json.load(f)


        return memories[-limit:]


    except:

        return []



def search_memory(
    keyword
):

    memories = get_memory(
        1000
    )


    results = []


    for item in memories:

        text = str(
            item.get(
                "content",
                ""
            )
        )


        if keyword.lower() in text.lower():

            results.append(
                item
            )


    return results



def clear_memory():

    file = memory_file()


    if file and file.exists():

        file.unlink()


    return True