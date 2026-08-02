def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "plan":
        return False

    print("📋 BearCore plan toimii.")

    return True