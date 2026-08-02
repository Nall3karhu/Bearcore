from datetime import datetime


def assistant(message=None):

    if message is None:

        message = input(
            "🐻 BearCore Assistant > "
        )


    if message.lower() == "poistu":

        return {

            "success": True,

            "message": "Assistant suljettu"

        }


    return {

        "success": True,

        "message": "🐻 BearCore Assistant vastasi",

        "data": {

            "input": message

        }

    }

    return {

        "success": True,

        "time": datetime.now().isoformat(),

        "message": "🐻 BearCore Assistant vastasi",

        "data": {

            "input": message

        }

    }