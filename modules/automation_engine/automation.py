from datetime import datetime



def create_task(
    action,
    target=None,
    data=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "action":
            action,

        "target":
            target,

        "data":
            data,

        "status":
            "created"

    }



def run_task(
    task
):

    if not task:

        return {

            "success": False,

            "message":
                "Tyhjä tehtävä"

        }



    task["status"] = "completed"


    return {

        "success": True,

        "task":
            task,

        "message":
            "⚙️ Tehtävä suoritettu"

    }



def create_automation(
    action,
    target=None
):

    task = create_task(
        action,
        target
    )


    return run_task(
        task
    )



def schedule_task(
    action,
    time=None
):

    return {

        "success": True,

        "action":
            action,

        "schedule":
            time,

        "message":
            "📅 Ajastus luotu"

    }