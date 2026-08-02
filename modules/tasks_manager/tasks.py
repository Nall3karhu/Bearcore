from datetime import datetime


def create_task(
    name,
    description=""
):

    return {

        "id":
            datetime.now().timestamp(),

        "name":
            name,

        "description":
            description,

        "status":
            "created",

        "created":
            datetime.now().isoformat()

    }



def start_task(
    task
):

    task["status"] = "running"

    return task



def complete_task(
    task
):

    task["status"] = "completed"

    task["completed"] = (
        datetime.now().isoformat()
    )

    return task



def fail_task(
    task,
    reason=""
):

    task["status"] = "failed"

    task["reason"] = reason

    return task



def get_status(
    task
):

    return {

        "task":
            task.get("name"),

        "status":
            task.get("status")

    }