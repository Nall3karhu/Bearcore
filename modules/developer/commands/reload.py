from core.module_manager import reload_modules


def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "reload":
        return False

    reload_modules()

    print("✅ Moduulit päivitetty.")

    return True