import json
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent


LOG_DIR = BASE_DIR / "logs"

LOG_FILE = LOG_DIR / "events.json"



def create_log():

    LOG_DIR.mkdir(
        exist_ok=True
    )


    if not LOG_FILE.exists():

        with open(
            LOG_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                [],
                f,
                indent=4
            )



def add_event(message):

    create_log()


    with open(
        LOG_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        events = json.load(f)



    events.append(
        {
            "time":
                datetime.now()
                .strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "event":
                message
        }
    )


    with open(
        LOG_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            events,
            f,
            indent=4,
            ensure_ascii=False
        )



def get_events():

    create_log()


    with open(
        LOG_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)