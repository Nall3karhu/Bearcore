from datetime import datetime



def create_decision(
    command,
    action,
    confidence=1.0
):

    return {

        "time":
            datetime.now().isoformat(),

        "command":
            command,

        "action":
            action,

        "confidence":
            confidence

    }



def decide(
    command
):

    if not command:

        return {

            "success": False,

            "message":
                "Tyhjä komento"

        }



    text = command.lower()



    rules = {


        "analysoi":
            "analyze",


        "analyze":
            "analyze",


        "testaa":
            "test",


        "test":
            "test",


        "backup":
            "backup",


        "varmuuskopio":
            "backup",


        "korjaa":
            "repair",


        "repair":
            "repair",


        "raportti":
            "report",


        "report":
            "report"


    }



    for word, action in rules.items():

        if word in text:

            return {

                "success": True,

                "decision":
                    create_decision(

                        command,

                        action,

                        0.9

                    )

            }



    return {

        "success": False,

        "decision":

            create_decision(

                command,

                "unknown",

                0.0

            )

    }



def get_action(
    command
):

    result = decide(
        command
    )


    if result["success"]:

        return (
            result["decision"]
            ["action"]
        )


    return None