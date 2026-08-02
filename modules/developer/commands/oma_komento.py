def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "oma_komento":
        return False

    print("🐻 BearCore oma_komento toimii.")

    return True