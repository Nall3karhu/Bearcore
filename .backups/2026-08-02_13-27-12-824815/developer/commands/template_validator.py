from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:
        print("❌ Anna templaten nimi")
        return False

    # Säilytetään nykyinen komentonimi yhteensopivuuden vuoksi
    if args[0].lower() != "template_validate":
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
        return False

    template_dir = base_dir / "templates" / template_name

    print("📋 Template Validator")
    print("====================")
    print()
    print(f"Tarkistetaan: {template_name}")
    print()

    if not template_dir.exists():

        print(f"❌ Templatea '{template_name}' ei löytynyt.")
        return False

    errors = []

    required_files = [
        "config.json"
    ]

    for filename in required_files:

        if (template_dir / filename).exists():

            print(f"✅ {filename}")

        else:

            print(f"❌ {filename}")

            errors.append(filename)

    if errors:

        print()
        print("Template ei läpäissyt tarkistusta.")

        return False

    print()
    print("✅ Template läpäisi tarkistuksen.")

    return True