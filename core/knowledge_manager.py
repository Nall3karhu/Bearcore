import json

from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

KNOWLEDGE_DIR = BASE_DIR / "knowledge"

DATABASE = KNOWLEDGE_DIR / "database.json"



def init_database():

    KNOWLEDGE_DIR.mkdir(
        exist_ok=True
    )


    if not DATABASE.exists():

        with open(
            DATABASE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                [],
                f,
                indent=4,
                ensure_ascii=False
            )



def load_knowledge():

    init_database()


    with open(
        DATABASE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_knowledge(data):

    with open(
        DATABASE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



def add_knowledge(
    topic,
    content,
    source="manual"
):

    data = load_knowledge()


    data.append(
        {
            "topic": topic,

            "content": content,

            "source": source,

            "time":
                datetime.now()
                .strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
        }
    )


    save_knowledge(
        data
    )


    return True



def search_knowledge(
    keyword
):

    data = load_knowledge()


    results = []


    for item in data:

        text = (
            item["topic"]
            +
            " "
            +
            item["content"]
        )


        if keyword.lower() in text.lower():

            results.append(
                item
            )


    return results