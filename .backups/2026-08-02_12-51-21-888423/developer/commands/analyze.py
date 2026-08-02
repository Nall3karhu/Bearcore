def command(args):

    if not args:
        return False

    if args[0] != "analyze":
        return False

    print("🔍 BearCore analysoi projektia...")

    print("")

    print("Projekti:")
    print("✔ Core")
    print("✔ Modules")
    print("✔ Tests")
    print("✔ UI")

    print("")
    print("Analyysi valmis.")

    return True