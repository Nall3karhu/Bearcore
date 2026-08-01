from modules.developer.planner import create_plan
from modules.developer.code_generator import create_code_module
from modules.developer.builder import build_module
from modules.developer.create_ui import create_ui



def command(args):


    if len(args) < 2:

        return False



    if args[0] == "plan" and args[1] == "module":

        create_plan(args[2:])

        return True



    if args[0] == "create" and args[1] == "module":

        create_code_module(args[2:])

        return True



    if args[0] == "build" and args[1] == "module":

        build_module(args[2:])

        return True



    if args[0] == "new" and args[1] == "ui":

        create_ui(args[2:])

        return True



    return False