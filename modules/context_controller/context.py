from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def context_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "context"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "context.json"
    )



def load_context():

    file = context_file()


    if not file or not file.exists():

        return {

            "history": []

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

            "history": []

        }



def save_context(
    data
):

    file = context_file()


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



def add_context(
    command,
    topic=None,
    status="active"
):

    context = load_context()


    entry = {

        "time":
            datetime.now().isoformat(),

        "command":
            command,

        "topic":
            topic,

        "status":
            status

    }


    context["history"].append(
        entry
    )


    save_context(
        context
    )


    return entry



def get_context():

    return load_context()



def get_last_context():

    context = load_context()


    history = context.get(
        "history",
        []
    )


    if not history:

        return None


    return history[-1]



def clear_context():

    file = context_file()


    if file and file.exists():

        file.unlink()


    return True



def context_status():

    return {

        "controller":
            "online",

        "entries":
            len(
                load_context()
                .get("history", [])
            ),

        "status":
            "ready"

    }