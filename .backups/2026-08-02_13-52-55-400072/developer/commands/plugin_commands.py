from modules.developer.plugin_creator import create_command


def command(args=None):

    if args is None:
        args = []

    if len(args) < 3:
        return False

    if args[0].lower() != "create":
        return False

    if args[1].lower() != "command":
        return False

    create_command(args[2])

    return True