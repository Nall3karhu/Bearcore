from pathlib import Path


def command(args):

    if len(args) < 1:
        return False


    if args[0] != "template_list":
        return False


    current = Path(__file__).resolve()

    base_dir = None


    for parent in current.parents:

        if parent.name == "BearCore":

            base_dir = parent
            break


    if base_dir is None:

        print("❌ BearCore-kansiota ei löytynyt.")
        return True


    templates_dir = base_dir / "templates"


    print("🐻 BearCore Templates")
    print("====================")


    if not templates_dir.exists():

        print("❌ Templates-kansiota ei löytynyt.")

        return True


    templates = []


    for item in templates_dir.iterdir():

        if item.is_dir():

            templates.append(
                item.name
            )


    templates.sort()


    for template in templates:

        print(
            f"✅ {template}"
        )


    print("")
    print(
        f"Yhteensä: {len(templates)} templatea"
    )


    return True