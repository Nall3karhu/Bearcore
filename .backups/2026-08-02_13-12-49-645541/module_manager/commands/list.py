from core.module_registry import all_modules


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "list":
        return False

    modules = all_modules()

    print("")
    print("=== Rekisteröidyt moduulit ===")
    print("")

    for name in sorted(modules.keys()):

        print(f"- {name}")

    return True