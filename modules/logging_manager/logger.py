from pathlib import Path
from datetime import datetime
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def log_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "logs"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "events.json"
    )



def load_logs():

    file = log_file()


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



def save_logs(
    logs
):

    file = log_file()


    if not file:

        return False


    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            logs,

            f,

            indent=4,

            ensure_ascii=False

        )


    return True



def create_log(
    level,
    message,
    module=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "level":
            level,

        "module":
            module,

        "message":
            message

    }



def write_log(
    level,
    message,
    module=None
):

    logs = load_logs()


    entry = create_log(

        level,

        message,

        module

    )


    logs.append(
        entry
    )


    save_logs(
        logs
    )


    return entry



def info(
    message,
    module=None
):

    return write_log(

        "INFO",

        message,

        module

    )



def warning(
    message,
    module=None
):

    return write_log(

        "WARNING",

        message,

        module

    )



def error(
    message,
    module=None
):

    return write_log(

        "ERROR",

        message,

        module

    )



def get_logs(
    limit=50
):

    logs = load_logs()


    return logs[-limit:]



def clear_logs():

    file = log_file()


    if file and file.exists():

        file.unlink()


    return True



def logger_status():

    return {

        "manager":
            "online",

        "logs":
            len(
                load_logs()
            )

    }