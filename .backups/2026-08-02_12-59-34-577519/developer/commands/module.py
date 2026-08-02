from core.module_manager import MODULES


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "modules":
        return False

    print("")
    print("=== Moduulit ===")

    for module in sorted(MODULES):
        print(f"- {module}")

    return True