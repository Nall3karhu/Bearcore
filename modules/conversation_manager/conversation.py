from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def conversation_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "conversations"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "history.json"
    )



def load_history():

    file = conversation_file()


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



def save_history(
    data
):

    file = conversation_file()


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



def create_message(
    role,
    text
):

    return {

        "time":
            datetime.now().isoformat(),

        "role":
            role,

        "text":
            text

    }



def add_message(
    role,
    text
):

    history = load_history()


    history.append(

        create_message(

            role,

            text

        )

    )


    save_history(
        history
    )


    return True



def get_messages(
    limit=50
):

    history = load_history()


    return history[-limit:]



def start_conversation(
    title="default"
):

    return {

        "id":
            datetime.now().timestamp(),

        "title":
            title,

        "started":
            datetime.now().isoformat(),

        "status":
            "active"

    }



def close_conversation():

    return {

        "status":
            "closed",

        "time":
            datetime.now().isoformat()

    }



def conversation_status():

    return {

        "manager":
            "online",

        "messages":
            len(
                load_history()
            )

    }