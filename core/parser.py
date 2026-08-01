def parse(text):

    text = text.strip().lower()

    if not text:
        return {
            "intent": "unknown"
        }

    # Muista...
    if text.startswith("muista"):
        return {
            "intent": "save",
            "text": text
        }

    # Hae...
    if text.startswith("hae"):
        return {
            "intent": "search",
            "text": text
        }

    # AI
    if text.startswith("ai"):
        return {
            "intent": "ai",
            "text": text
        }

    # Sisäänrakennetut komennot
    if text in (
        "apu",
        "help",
        "exit",
        "quit",
        "lopeta",
        "status",
        "version"
    ):
        return {
            "intent": "command",
            "command": text
        }

    # Moduulit
    osat = text.split()

    return {
        "intent": "module",
        "module": osat[0],
        "args": osat[1:]
    }