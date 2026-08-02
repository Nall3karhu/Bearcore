from datetime import datetime
from pathlib import Path
import json



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def learning_file():

    base = find_bearcore()

    if not base:

        return None


    folder = base / "learning"

    folder.mkdir(
        exist_ok=True
    )


    return folder / "learning.json"



def load_learning():

    file = learning_file()


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



def save_learning(data):

    file = learning_file()


    if not file:

        return False


    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


    return True



def create_learning_entry(
    topic,
    information,
    source=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "topic":
            topic,

        "information":
            information,

        "source":
            source,

        "importance":
            "normal"

    }



def learn(
    topic,
    information,
    source=None
):

    data = load_learning()


    entry = create_learning_entry(

        topic,

        information,

        source

    )


    data.append(
        entry
    )


    save_learning(
        data
    )


    return entry



def search_learning(
    keyword
):

    data = load_learning()


    results = []


    for item in data:

        text = str(
            item
        ).lower()


        if keyword.lower() in text:

            results.append(
                item
            )


    return results



def learning_status():

    return {

        "controller":
            "online",

        "learned_items":
            len(
                load_learning()
            ),

        "status":
            "ready"

    }