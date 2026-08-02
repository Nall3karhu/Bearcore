from datetime import datetime

from modules.knowledge_controller.controller import process_query



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



def create_research_task(
    topic
):

    return {

        "topic":
            topic,

        "status":
            "created",

        "created":
            datetime.now().isoformat()

    }



def analyze_topic(
    topic
):

    if not topic:

        return create_response(

            False,

            "Aihe puuttuu"

        )



    knowledge = process_query(
        topic
    )


    return create_response(

        True,

        "Tutkimus valmis",

        {

            "topic":
                topic,

            "knowledge":
                knowledge

        }

    )



def save_research(
    result
):

    return {

        "status":
            "stored",

        "time":
            datetime.now().isoformat(),

        "data":
            result

    }



def research(
    topic
):

    task = create_research_task(
        topic
    )


    analysis = analyze_topic(
        topic
    )


    saved = save_research(
        analysis
    )


    return create_response(

        True,

        "Tutkimusprosessi valmis",

        {

            "task":
                task,

            "analysis":
                analysis,

            "saved":
                saved

        }

    )



def research_status():

    return {

        "engine":
            "online",

        "status":
            "ready"

    }