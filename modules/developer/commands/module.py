from core.module_manager import MODULES


def command(args=None):

    if args is None:
        args = []

    if len(args) == 0:
        return False

    if args[0].lower() != "modules":
        return False

    print("")
    print("=== Moduulit ===")

    for module in sorted(MODULES):
        print(f"- {module}")

    return True