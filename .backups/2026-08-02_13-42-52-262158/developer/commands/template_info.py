import json
from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:
        print("❌ Anna templaten nimi")
        return False

    if args[0].lower() != "template_info":
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

    if not template_dir.exists():

        print(f"❌ Templatea '{template_name}' ei löytynyt.")
        return False

    print("📄 Template Info")
    print("================")
    print(f"Nimi: {template_name}")
    print()

    config_file = template_dir / "config.json"

    try:

        if config_file.exists():

            with config_file.open(
                "r",
                encoding="utf-8"
            ) as f:

                config = json.load(f)

            print(f"Versio: {config.get('version', 'ei määritetty')}")
            print(f"Kategoria: {config.get('category', 'ei määritetty')}")
            print(f"Kuvaus: {config.get('description', 'ei määritetty')}")

        print()
        print("Tiedostot:")
        print()

        for file in sorted(template_dir.iterdir()):

            if file.is_file():

                print(f"✅ {file.name}")

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Template-tietojen luku epäonnistui: {e}")

        return False