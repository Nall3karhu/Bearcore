from core.knowledge_manager import (
    add_knowledge,
    search_knowledge,
    load_knowledge
)



def knowledge(args):


    print(
        "DEBUG ARGS:",
        args
    )


    if not args:

        print(
"""
📚 Knowledge komennot:

knowledge add <aihe> <teksti>

knowledge search <hakusana>

knowledge list
"""
        )

        return True



    command = args[0].lower()



    # -------------------------
    # ADD
    # -------------------------

    if command == "add":


        if len(args) < 3:

            print(
                "❌ Käyttö: knowledge add <aihe> <teksti>"
            )

            return True



        topic = args[1]


        content = " ".join(
            args[2:]
        )


        add_knowledge(
            topic,
            content,
            "knowledge"
        )


        print(
            f"✅ Tallennettu: {topic}"
        )


        return True



    # -------------------------
    # SEARCH
    # -------------------------

    if command == "search":


        if len(args) < 2:

            print(
                "❌ Käyttö: knowledge search <hakusana>"
            )

            return True



        results = search_knowledge(
            args[1]
        )



        if not results:

            print(
                "📂 Ei löytynyt"
            )

            return True



        print(
            "📚 Löydetyt tiedot:"
        )



        for item in results:

            print(
f"""
📌 {item['topic']}

{item['content']}

🕒 {item['time']}

----------------
"""
            )


        return True



    # -------------------------
    # LIST
    # -------------------------

    if command == "list":


        data = load_knowledge()



        if not data:

            print(
                "📂 Muisti on tyhjä"
            )

            return True



        print(
            "📚 BearCore Knowledge\n"
        )



        for i, item in enumerate(
            data,
            1
        ):

            print(
                f"{i}. {item['topic']}"
            )


        return True



    print(
        "❌ Tuntematon knowledge-komento:"
        ,
        command
    )


    return True