from core.module_manager import reload_modules


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "reload":
        return False

    reload_modules()

    print("✅ Moduulit päivitetty.")

    return True