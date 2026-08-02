from core.module_registry import all_modules


def command(args):

    if len(args) < 2:
        return False

    if args[0] != "search":
        return False

    keyword = args[1].lower()

    modules = all_modules()

    print("")
    print(f"🔍 Hakutulokset: '{keyword}'")
    print("-" * 40)

    found = False

    for name, info in sorted(modules.items()):

        aliases = info.get("aliases", [])
        category = info.get("category", "")
        description = info.get("description", "")

        text = " ".join([
            name,
            category,
            description,
            " ".join(aliases)
        ]).lower()

        if keyword in text:

            print(f"✓ {name}")
            found = True

    if not found:

        print("Ei hakutuloksia.")

    print("-" * 40)

    return True