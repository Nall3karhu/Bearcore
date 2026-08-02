from datetime import datetime



def create_schedule(
    task,
    time
):

    return {

        "task":
            task,

        "time":
            time,

        "created":
            datetime.now().isoformat(),

        "status":
            "waiting"

    }



def run_schedule(
    task
):

    return {

        "success":
            True,

        "task":
            task,

        "status":
            "completed"

    }



def list_schedule():

    return []