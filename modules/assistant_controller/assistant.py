from datetime import datetime



def create_response(
    message,
    action=None,
    success=True
):

    return {

        "success": success,

        "time":
            datetime.now().isoformat(),

        "message":
            message,

        "action":
            action

    }



def process_command(
    command
):

    if not command:

        return create_response(
            "❌ Tyhjä komento",
            None,
            False
        )



    command = command.lower()



    if "analysoi" in command:

        return create_response(
            "🔍 Analysointi käynnistetty",
            "analyze"
        )



    if "testaa" in command:

        return create_response(
            "🧪 Testaus käynnistetty",
            "test"
        )



    if "backup" in command:

        return create_response(
            "💾 Backup käynnistetty",
            "backup"
        )



    if "raportti" in command:

        return create_response(
            "📊 Raportti luotu",
            "report"
        )



    return create_response(

        "🤖 En tunnistanut komentoa",

        "unknown",

        False

    )



def ask(
    text
):

    return process_command(
        text
    )