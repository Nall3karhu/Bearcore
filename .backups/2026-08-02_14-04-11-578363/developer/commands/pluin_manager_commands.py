from modules.developer.plugin_manager import (
    list_plugins,
    remove_plugin
)


def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() == "plugins":

        list_plugins()

        return True


    if len(args) >= 3:

        if args[0].lower() == "remove" and args[1].lower() == "plugin":

            remove_plugin(args[2:])

            return True


    return False