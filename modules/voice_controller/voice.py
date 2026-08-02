from datetime import datetime



def response(
    success,
    message,
    data=None
):

    return {

        "success": success,

        "time":
            datetime.now().isoformat(),

        "message":
            message,

        "data":
            data

    }



def listen():

    return response(

        True,

        "🎙️ Kuuntelu valmis",

        None

    )



def recognize(
    audio=None
):

    return response(

        True,

        "🗣️ Puhe tunnistettu",

        audio

    )



def speak(
    text
):

    return response(

        True,

        "🔊 Puhe muodostettu",

        text

    )



def voice_command(
    text
):

    return response(

        True,

        "🎤 Äänikomento vastaanotettu",

        text

    )