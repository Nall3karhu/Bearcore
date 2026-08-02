from datetime import datetime



def create_project(
    name,
    description=""
):

    return {

        "name":
            name,

        "description":
            description,

        "created":
            datetime.now().isoformat(),

        "status":
            "active"

    }



def add_task(
    project,
    task
):

    return {

        "project":
            project,

        "task":
            task,

        "status":
            "added"

    }



def update_status(
    project,
    status
):

    return {

        "project":
            project,

        "status":
            status

    }



def get_project(
    name
):

    return {

        "name":
            name,

        "status":
            "active"

    }



def list_projects():

    return []