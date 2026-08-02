from datetime import datetime


from modules.learning_controller.learning import learn

from modules.memory_controller.memory import remember

from modules.conversation_controller.conversation import (
    add_user_message,
    add_assistant_message
)

from modules.context_controller.context import (
    add_context
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



def process_learning_conversation(
    user_message,
    assistant_response,
    topic=None
):

    if not topic:

        topic = user_message



    conversation_user = add_user_message(
        user_message
    )


    conversation_assistant = add_assistant_message(
        assistant_response
    )


    context = add_context(

        user_message,

        topic

    )


    memory = remember(

        "assistant_learning",

        {

            "user":
                user_message,

            "assistant":
                assistant_response

        },

        "assistant"

    )


    learned = learn(

        topic,

        assistant_response,

        "assistant"

    )


    return create_response(

        True,

        "Assistant oppi keskustelusta",

        {

            "conversation_user":
                conversation_user,

            "conversation_assistant":
                conversation_assistant,

            "context":
                context,

            "memory":
                memory,

            "learning":
                learned

        }

    )



def assistant_learning_status():

    return {

        "module":
            "assistant_learning",

        "status":
            "ready"

    }