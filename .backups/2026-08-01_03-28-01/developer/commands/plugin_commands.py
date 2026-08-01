from modules.developer.plugin_creator import create_command


def command(args):

    if len(args) >= 3:

        if args[0] == "create" and args[1] == "command":

            create_command(args[2])

            return True


    return False