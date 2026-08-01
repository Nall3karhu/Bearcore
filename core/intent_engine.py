def detect(command):

    text = command.strip().lower()

    if text.startswith("luo "):

        parts = text.split()

        if len(parts) >= 2:

            if parts[1] == "moduuli":

                if len(parts) >= 3:
                    return f"developer create {parts[2]}"

            return f"developer create {parts[1]}"

    if text.startswith("tee uusi moduuli"):

        parts = text.split()

        if len(parts) >= 4:
            return f"developer create {parts[3]}"

    if text.startswith("haluan uuden moduulin"):

        parts = text.split()

        if len(parts) >= 4:
            return f"developer create {parts[-1]}"

    return command