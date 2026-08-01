from modules.developer.plugin_manager import (
    list_plugins,
    remove_plugin
)



def command(args):


    if args[0] == "plugins":

        list_plugins()

        return True



    if len(args) >= 3:


        if args[0] == "remove" and args[1] == "plugin":

            remove_plugin(args[2:])

            return True



    return False