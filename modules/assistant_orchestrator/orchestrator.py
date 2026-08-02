from datetime import datetime


from modules.command_router.router import route


from modules.status_controller.status import (
    format_status
)


from modules.assistant_research.research_bridge import (
    research_topic
)


from modules.response_formatter.cleaner import (
    clean_research_response
)



def create_response(
    success,
    message,
    data=None
):

    return {

        "success":
            success,

        "time":
            datetime.now().isoformat(),

        "message":
            message,

        "data":
            data

    }



def decide_action(
    target
):

    actions = {

        "health":
            "Järjestelmän tarkistus",

        "backup":
            "Varmuuskopiointi",

        "self_test":
            "Testaus",

        "registry":
            "Moduulien tarkistus",

        "update":
            "Päivitysten tarkistus",

        "assistant":
            "Yleinen käsittely"

    }


    return actions.get(

        target,

        "Tuntematon toiminto"

    )



def is_research_command(
    command
):

    words = [

        "tutki",

        "etsi",

        "hae",

        "selvitä",

        "tietoa"

    ]


    command = command.lower()


    return any(

        word in command

        for word in words

    )



def extract_topic(
    command
):

    remove = [

        "tutki",

        "etsi",

        "hae",

        "selvitä",

        "tietoa"

    ]


    topic = command.lower()


    for word in remove:

        topic = topic.replace(

            word,

            ""

        )


    return topic.strip()



def ask(
    command
):


    if is_research_command(
        command
    ):

        topic = extract_topic(
            command
        )


        result = research_topic(
            topic
        )


        return {

            "success":
                result["success"],

            "time":
                result["time"],

            "message":
                clean_research_response(

                    result

                ),

            "data":
                result["data"]

        }



    routed = route(
        command
    )


    if not routed["success"]:

        return create_response(

            False,

            "Komennon käsittely epäonnistui"

        )



    target = routed["target"]



    if command.lower().strip() == "status":

        return create_response(

            True,

            format_status(),

            {

                "command":
                    command,

                "target":
                    target

            }

        )



    action = decide_action(
        target
    )


    return create_response(

        True,

        action,

        {

            "command":
                command,

            "target":
                target

        }

    )



def orchestrator_status():

    return {

        "assistant":
            "online",

        "status":
            "ready"

    }