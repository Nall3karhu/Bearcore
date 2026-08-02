def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "think":
        return False

    print("💭 BearCore think toimii.")

    return True