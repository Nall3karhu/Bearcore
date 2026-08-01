from difflib import get_close_matches


def suggest(command, commands):

    match = get_close_matches(
        command.lower(),
        commands,
        n=1,
        cutoff=0.60
    )

    if match:
        return match[0]

    return None