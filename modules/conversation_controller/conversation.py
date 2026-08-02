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
        "conversation"
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
    history
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

            history,

            f,

            indent=4,

            ensure_ascii=False

        )


    return True



def create_message(
    role,
    content
):

    return {

        "time":
            datetime.now().isoformat(),

        "role":
            role,

        "content":
            content

    }



def add_message(
    role,
    content
):

    history = load_history()


    message = create_message(

        role,

        content

    )


    history.append(
        message
    )


    save_history(
        history
    )


    return message



def add_user_message(
    content
):

    return add_message(

        "user",

        content

    )



def add_assistant_message(
    content
):

    return add_message(

        "assistant",

        content

    )



def get_history(
    limit=50
):

    history = load_history()


    return history[-limit:]



def get_last_message():

    history = load_history()


    if not history:

        return None


    return history[-1]



def clear_history():

    file = conversation_file()


    if file and file.exists():

        file.unlink()


    return True



def conversation_status():

    return {

        "controller":
            "online",

        "messages":
            len(
                load_history()
            ),

        "status":
            "ready"

    }