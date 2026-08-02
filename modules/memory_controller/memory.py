from datetime import datetime
from pathlib import Path
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


    folder = (
        base /
        "memory"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "memory.json"
    )



def load_memory():

    file = memory_file()


    if not file or not file.exists():

        return []


    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return []



def save_memory(
    data
):

    file = memory_file()


    if not file:

        return False


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



def create_memory(
    memory_type,
    content,
    source=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "type":
            memory_type,

        "content":
            content,

        "source":
            source

    }



def remember(
    memory_type,
    content,
    source=None
):

    memories = load_memory()


    entry = create_memory(

        memory_type,

        content,

        source

    )


    memories.append(
        entry
    )


    save_memory(
        memories
    )


    return entry



def get_memory(
    limit=50
):

    memories = load_memory()


    return memories[-limit:]



def search_memory(
    keyword
):

    memories = load_memory()


    results = []


    for item in memories:

        text = str(
            item
        ).lower()


        if keyword.lower() in text:

            results.append(
                item
            )


    return results



def clear_memory():

    file = memory_file()


    if file and file.exists():

        file.unlink()


    return True



def memory_status():

    return {

        "controller":
            "online",

        "memories":
            len(
                load_memory()
            ),

        "status":
            "ready"

    }