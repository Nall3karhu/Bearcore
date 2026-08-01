from modules.developer.plugin_backup import (
    backup_plugin,
    restore_plugin
)



def command(args):


    if len(args) >= 3:


        if args[0] == "backup" and args[1] == "plugin":

            backup_plugin(args[2:])

            return True



        if args[0] == "restore" and args[1] == "plugin":

            restore_plugin(args[2:])

            return True



    return False