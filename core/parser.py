def parse(text):

    text = text.strip().lower()

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

    # Moduulit
    osat = text.split()

    if len(osat):

        return {
            "intent": "module",
            "module": osat[0],
            "args": osat[1:]
        }

    return {
        "intent": "unknown"
    }