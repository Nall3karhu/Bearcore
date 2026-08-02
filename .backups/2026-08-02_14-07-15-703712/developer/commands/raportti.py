def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "raportti":
        return False

    print("🐻 BearCore raportti toimii.")

    return True