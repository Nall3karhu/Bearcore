from datetime import datetime


from modules.web_research.search import (
    research_web
)


from modules.research_reader.connector import (
    analyze_research_sources
)


from modules.knowledge_bridge.bridge import (
    save_knowledge
)


from modules.learning_controller.learning import (
    learn
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



def research_topic(
    topic
):


    web_result = research_web(
        topic
    )


    if not web_result["success"]:

        return create_response(

            False,

            "Web-haku epäonnistui"

        )


    results = web_result["data"]["results"]



    research = analyze_research_sources(

        topic,

        results

    )



    knowledge = save_knowledge(

        topic

    )



    learned = learn(

        topic,

        str(
            research["summary"]
        ),

        "research"

    )



    return create_response(

        True,

        "🐻 BearCore tutkimus valmis",

        {

            "web":
                web_result,

            "research":
                research,

            "knowledge":
                knowledge,

            "learning":
                learned

        }

    )



def research_bridge_status():

    return {

        "module":
            "assistant_research",

        "status":
            "ready"

    }