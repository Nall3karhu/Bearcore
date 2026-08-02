from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def schedule_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "scheduler"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "tasks.json"
    )



def load_tasks():

    file = schedule_file()


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



def save_tasks(
    tasks
):

    file = schedule_file()


    if not file:

        return False


    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            tasks,

            f,

            indent=4,

            ensure_ascii=False

        )


    return True



def create_task(
    name,
    action,
    schedule
):

    return {

        "id":
            datetime.now().timestamp(),

        "name":
            name,

        "action":
            action,

        "schedule":
            schedule,

        "status":
            "waiting",

        "created":
            datetime.now().isoformat()

    }



def add_task(
    name,
    action,
    schedule
):

    tasks = load_tasks()


    task = create_task(

        name,

        action,

        schedule

    )


    tasks.append(
        task
    )


    save_tasks(
        tasks
    )


    return task



def get_tasks():

    return load_tasks()



def run_task(
    task_id
):

    tasks = load_tasks()


    for task in tasks:

        if task["id"] == task_id:

            task["status"] = "running"

            task["started"] = (
                datetime.now()
                .isoformat()
            )


    save_tasks(
        tasks
    )


    return True



def complete_task(
    task_id
):

    tasks = load_tasks()


    for task in tasks:

        if task["id"] == task_id:

            task["status"] = "completed"

            task["completed"] = (
                datetime.now()
                .isoformat()
            )


    save_tasks(
        tasks
    )


    return True



def scheduler_status():

    return {

        "manager":
            "online",

        "tasks":
            len(
                load_tasks()
            )

    }