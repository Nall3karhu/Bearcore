from core.project import PROJECT_ROOT


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "pwd":
        return False

    print(f"📂 {PROJECT_ROOT}")

    return True