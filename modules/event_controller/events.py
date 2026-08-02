from pathlib import Path
from datetime import datetime
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def event_response(
    success=True,
    message=""
):

    return {

        "success": success,

        "time":
            datetime.now().isoformat(),

        "message":
            message

    }



def event_file():

    base = find_bearcore()

    if not base:

        return None


    logs = (
        base /
        "logs"
    )

    logs.mkdir(
        exist_ok=True
    )


    return (
        logs /
        "events.json"
    )



def save_event(message):

    file = event_file()


    if not file:

        return event_response(
            False,
            "Logikansiota ei löytynyt"
        )


    events = []


    if file.exists():

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                events = json.load(f)


        except:

            events = []



    events.append({

        "time":
            datetime.now().isoformat(),

        "event":
            message

    })



    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            events,
            f,
            indent=4,
            ensure_ascii=False
        )


    return event_response(
        True,
        message
    )



def get_events(limit=20):

    file = event_file()


    if not file or not file.exists():

        return []



    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            events = json.load(f)


        return events[-limit:]


    except:

        return []



def clear_events():

    file = event_file()


    if file and file.exists():

        file.unlink()


    return event_response(
        True,
        "Eventit poistettu"
    )