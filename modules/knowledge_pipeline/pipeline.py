from datetime import datetime



def create_item(
    topic,
    content,
    source=None
):

    return {

        "time":
            datetime.now().isoformat(),

        "topic":
            topic,

        "content":
            content,

        "source":
            source

    }



def process(
    topic,
    content,
    source=None
):

    item = create_item(
        topic,
        content,
        source
    )


    return {

        "success":
            True,

        "message":
            "🧠 Tieto käsitelty",

        "data":
            item

    }



def connect_memory(
    item
):

    return {

        "success":
            True,

        "message":
            "💾 Yhdistetty muistiin",

        "data":
            item

    }



def connect_knowledge(
    item
):

    return {

        "success":
            True,

        "message":
            "📚 Yhdistetty tietokantaan",

        "data":
            item

    }