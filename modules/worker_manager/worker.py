from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def worker_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "workers"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "workers.json"
    )



def load_workers():

    file = worker_file()


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



def save_workers(
    data
):

    file = worker_file()


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



def create_worker(
    name
):

    return {

        "name":
            name,

        "status":
            "idle",

        "created":
            datetime.now().isoformat()

    }



def register_worker(
    name
):

    workers = load_workers()


    worker = create_worker(
        name
    )


    workers.append(
        worker
    )


    save_workers(
        workers
    )


    return worker



def list_workers():

    return load_workers()



def start_worker(
    name
):

    workers = load_workers()


    for worker in workers:

        if worker["name"] == name:

            worker["status"] = "running"


    save_workers(
        workers
    )


    return True



def stop_worker(
    name
):

    workers = load_workers()


    for worker in workers:

        if worker["name"] == name:

            worker["status"] = "stopped"


    save_workers(
        workers
    )


    return True



def execute_task(
    worker,
    task
):

    return {

        "worker":
            worker,

        "task":
            task,

        "status":
            "completed",

        "time":
            datetime.now().isoformat()

    }



def worker_status():

    return {

        "manager":
            "online",

        "workers":
            len(
                load_workers()
            )

    }