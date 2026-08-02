from datetime import datetime


from modules.research_connector.research import research



def save_knowledge(
    topic
):

    result = research(
        topic
    )


    return {

        "success":
            True,

        "time":
            datetime.now().isoformat(),

        "message":
            "Tieto tallennettu",

        "data":
            result

    }



def knowledge_bridge_status():

    return {

        "module":
            "knowledge_bridge",

        "status":
            "ready"

    }