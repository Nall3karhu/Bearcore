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

            "session": [],

            "current_task": None,

            "topic": None

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

            "session": [],

            "current_task": None,

            "topic": None

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



def add_message(
    role,
    message
):

    context = load_context()


    context["session"].append({

        "time":
            datetime.now().isoformat(),

        "role":
            role,

        "message":
            message

    })


    save_context(
        context
    )


    return True



def set_topic(
    topic
):

    context = load_context()


    context["topic"] = topic


    save_context(
        context
    )


    return True



def get_topic():

    context = load_context()


    return context.get(
        "topic"
    )



def set_task(
    task
):

    context = load_context()


    context["current_task"] = task


    save_context(
        context
    )


    return True



def get_task():

    context = load_context()


    return context.get(
        "current_task"
    )



def get_history(
    limit=20
):

    context = load_context()


    return context["session"][-limit:]



def clear_context():

    file = context_file()


    if file and file.exists():

        file.unlink()


    return True



def context_status():

    context = load_context()


    return {

        "messages":
            len(
                context["session"]
            ),

        "topic":
            context["topic"],

        "status":
            "online"

    }