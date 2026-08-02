from modules.developer.planner import create_plan
from modules.developer.code_generator import create_code_module
from modules.developer.builder import build_module
from modules.developer.create_ui import create_ui


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:
        return False

    cmd = args[0].lower()
    target = args[1].lower()


    if cmd == "plan" and target == "module":

        create_plan(args[2:])

        return True


    if cmd == "create" and target == "module":

        create_code_module(args[2:])

        return True


    if cmd == "build" and target == "module":

        build_module(args[2:])

        return True


    if cmd == "new" and target == "ui":

        create_ui(args[2:])

        return True


    return False