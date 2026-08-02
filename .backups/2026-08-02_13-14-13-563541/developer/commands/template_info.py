import json
from pathlib import Path


def command(args):

    if len(args) < 2:
        return False


    if args[0] != "template_info":
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


    if not template_dir.exists():

        print(
            f"❌ Template '{template_name}' ei löytynyt."
        )

        return True


    print("🐻 Template Info")
    print("================")
    print(
        f"Nimi: {template_name}"
    )

    print("")


    config_file = template_dir / "config.json"


    if config_file.exists():

        with open(
            config_file,
            "r",
            encoding="utf-8"
        ) as f:

            config = json.load(f)


        print(
            f"Versio: {config.get('version', 'ei määritetty')}"
        )

        print(
            f"Kategoria: {config.get('category', 'ei määritetty')}"
        )

        print(
            f"Kuvaus: {config.get('description', 'ei määritetty')}"
        )


    print("")

    print("Tiedostot:")
    print("")


    for file in template_dir.iterdir():

        if file.is_file():

            print(
                f"✅ {file.name}"
            )


    return True