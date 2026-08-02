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


    folder = (
        base /
        "learning"
    )


    folder.mkdir(
        exist_ok=True
    )


    return (
        folder /
        "lessons.json"
    )



def create_lesson(
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
            source

    }



def teach(
    topic,
    information,
    source=None
):

    file = learning_file()


    if not file:

        return False


    lessons = []


    if file.exists():

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                lessons = json.load(f)

        except:

            lessons = []



    lessons.append(
        create_lesson(
            topic,
            information,
            source
        )
    )



    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            lessons,
            f,
            indent=4,
            ensure_ascii=False
        )


    return True



def get_lessons():

    file = learning_file()


    if not file or not file.exists():

        return []


    with open(
        file,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def search_lessons(
    keyword
):

    lessons = get_lessons()

    results = []


    for lesson in lessons:

        text = str(
            lesson
        )


        if keyword.lower() in text.lower():

            results.append(
                lesson
            )


    return results