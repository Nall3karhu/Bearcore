from datetime import datetime

from modules.web_research.providers.basic_search import (
    search_web
)


def research_web(query):

    result = search_web(
        query
    )

    return {

        "success":
            result["success"],

        "time":
            datetime.now().isoformat(),

        "message":
            "🔎 Web tutkimus valmis",

        "data":
            result

    }



def web_status():

    return {

        "module":
            "web_research",

        "status":
            "ready"

    }