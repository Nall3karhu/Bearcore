from datetime import datetime


from modules.memory_controller.memory import remember

from modules.context_controller.context import add_context

from modules.conversation_controller.conversation import (
    add_user_message,
    add_assistant_message
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



def save_user_input(
    message
):

    return add_user_message(
        message
    )



def save_context(
    message
):

    return add_context(

        message,

        topic=message

    )



def save_memory(
    message,
    response
):

    return remember(

        "conversation",

        {

            "user":
                message,

            "assistant":
                response

        },

        "assistant"

    )



def save_assistant_response(
    response
):

    return add_assistant_message(
        response
    )



def process_conversation(
    message,
    response
):

    user = save_user_input(
        message
    )


    context = save_context(
        message
    )


    assistant = save_assistant_response(
        response
    )


    memory = save_memory(

        message,

        response

    )


    return create_response(

        True,

        "Keskustelu tallennettu",

        {

            "user":
                user,

            "context":
                context,

            "assistant":
                assistant,

            "memory":
                memory

        }

    )



def memory_bridge_status():

    return {

        "module":
            "assistant_memory",

        "status":
            "ready"

    }