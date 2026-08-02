from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def queue_file():

    base = find_bearcore()

    if not base:

        return None


    folder = base / "queue"

    folder.mkdir(
        exist_ok=True
    )


    return folder / "messages.json"



def load_queue():

    file = queue_file()


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



def save_queue(
    data
):

    file = queue_file()


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
    action,
    data=None,
    priority="normal"
):

    return {

        "id":
            datetime.now().timestamp(),

        "time":
            datetime.now().isoformat(),

        "action":
            action,

        "priority":
            priority,

        "data":
            data,

        "status":
            "waiting"

    }



def add_message(
    action,
    data=None,
    priority="normal"
):

    queue = load_queue()


    message = create_message(
        action,
        data,
        priority
    )


    queue.append(
        message
    )


    save_queue(
        queue
    )


    return message



def get_messages():

    return load_queue()



def next_message():

    queue = load_queue()


    if not queue:

        return None


    return queue[0]



def complete_message(
    message_id
):

    queue = load_queue()


    for item in queue:

        if item["id"] == message_id:

            item["status"] = "completed"


    save_queue(
        queue
    )


    return True



def queue_status():

    return {

        "manager":
            "online",

        "messages":
            len(
                load_queue()
            )

    }