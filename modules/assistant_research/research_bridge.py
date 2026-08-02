from datetime import datetime


from modules.web_research.search import (
    research_web
)


from modules.research_analyzer.analyzer import (
    analyze_results,
    format_analysis
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


    analysis = analyze_results(

        topic,

        results

    )


    knowledge = save_knowledge(
        topic
    )


    learned = learn(

        topic,

        analysis["summary"],

        "web_research"

    )


    response = format_analysis(
        analysis
    )


    return create_response(

        True,

        response,

        {

            "web":
                web_result,

            "analysis":
                analysis,

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