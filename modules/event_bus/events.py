from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def event_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "events"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "events.json"
    )



def load_events():

    file = event_file()


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



def save_events(
    events
):

    file = event_file()


    if not file:

        return False


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


    return True



def create_event(
    name,
    data=None,
    source=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "name":
            name,

        "source":
            source,

        "data":
            data

    }



def emit(
    name,
    data=None,
    source=None
):

    events = load_events()


    event = create_event(

        name,

        data,

        source

    )


    events.append(
        event
    )


    save_events(
        events
    )


    return event



def get_events(
    limit=50
):

    events = load_events()


    return events[-limit:]



def find_events(
    name
):

    events = load_events()


    results = []


    for event in events:

        if event["name"] == name:

            results.append(
                event
            )


    return results



def clear_events():

    file = event_file()


    if file and file.exists():

        file.unlink()


    return True



def event_status():

    return {

        "bus":
            "online",

        "events":
            len(
                load_events()
            )

    }