from datetime import datetime



def create_event(
    name,
    value=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "name":
            name,

        "value":
            value

    }



def track(
    name,
    value=None
):

    return create_event(
        name,
        value
    )



def statistics():

    return {

        "events":
            0,

        "status":
            "ready"

    }



def report():

    return {

        "title":
            "BearCore Analytics",

        "status":
            "ready"

    }