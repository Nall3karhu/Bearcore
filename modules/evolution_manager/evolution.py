from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def evolution_file():

    base = find_bearcore()

    if not base:

        return None


    folder = (
        base /
        "evolution"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "ideas.json"
    )



def load_ideas():

    file = evolution_file()


    if not file or not file.exists():

        return []


    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return []



def save_ideas(
    ideas
):

    file = evolution_file()


    if not file:

        return False


    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            ideas,

            f,

            indent=4,

            ensure_ascii=False

        )


    return True



def create_idea(
    title,
    description,
    priority="normal"
):

    return {

        "time":
            datetime.now().isoformat(),

        "title":
            title,

        "description":
            description,

        "priority":
            priority,

        "status":
            "planned"

    }



def add_idea(
    title,
    description,
    priority="normal"
):

    ideas = load_ideas()


    idea = create_idea(

        title,

        description,

        priority

    )


    ideas.append(
        idea
    )


    save_ideas(
        ideas
    )


    return idea



def list_ideas():

    return load_ideas()



def improve_module(
    module,
    reason
):

    return {

        "module":
            module,

        "reason":
            reason,

        "status":
            "review"

    }



def evolution_status():

    return {

        "manager":
            "online",

        "ideas":
            len(
                load_ideas()
            ),

        "mode":
            "learning"

    }