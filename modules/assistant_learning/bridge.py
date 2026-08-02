from datetime import datetime

from modules.learning_controller.learning import learn



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



def learn_from_conversation(
    topic,
    information
):

    result = learn(

        topic,

        information,

        "assistant"

    )


    return create_response(

        True,

        "Tieto opittu",

        result

    )



def learning_bridge_status():

    return {

        "module":
            "assistant_learning",

        "status":
            "ready"

    }