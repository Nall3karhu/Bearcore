from pathlib import Path


def command(args):

    if len(args) < 2:
        return False


    if args[0] != "template_validate":
        return False


    template_name = args[1].strip().lower()


    current = Path(__file__).resolve()

    base_dir = None


    for parent in current.parents:

        if parent.name == "BearCore":

            base_dir = parent
            break


    if base_dir is None:

        print("❌ BearCore-kansiota ei löytynyt.")
        return True


    template_dir = (
        base_dir /
        "templates" /
        template_name
    )


    print("🐻 Template Validator")
    print("====================")
    print("")
    print(f"Tarkistetaan: {template_name}")
    print("")


    if not template_dir.exists():

        print(
            f"❌ Template '{template_name}' ei löytynyt."
        )

        return True


    required_files = [

        "config.json",
        "README.md",
        "template.py",
        "__init__.py"

    ]


    errors = []


    for file in required_files:

        path = template_dir / file


        if path.exists():

            print(
                f"✅ {file} löytyy"
            )

        else:

            print(
                f"❌ {file} puuttuu"
            )

            errors.append(file)



    print("")


    if errors:

        print("❌ Template ei ole kunnossa")

        return True



    print("✅ Template kunnossa")


    return True