from modules.developer.plugin_backup import (
    backup_plugin,
    restore_plugin
)


def command(args=None):

    if args is None:
        args = []

    if len(args) < 3:
        return False

    if args[0].lower() == "backup" and args[1].lower() == "plugin":

        backup_plugin(args[2:])

        return True


    if args[0].lower() == "restore" and args[1].lower() == "plugin":

        restore_plugin(args[2:])

        return True


    return False