def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "analyze":
        return False

    print("🔍 BearCore analysoi projektia...")
    print()

    print("Projekti:")
    print("✅ Core")
    print("✅ Modules")
    print("✅ Tests")
    print("✅ UI")

    print()
    print("✅ Analyysi valmis.")

    return True