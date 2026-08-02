def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "review":
        return False

    print("🔎 BearCore review toimii.")

    return True