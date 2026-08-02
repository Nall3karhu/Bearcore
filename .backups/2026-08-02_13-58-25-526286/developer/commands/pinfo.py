import json
from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "pinfo":
        return False

    current = Path(__file__).resolve()

    base_dir = None

    for parent in current.parents:

        if parent.name == "BearCore":

            base_dir = parent
            break

    if base_dir is None:

        print("❌ BearCore-kansiota ei löytynyt.")
        return False

    config_file = base_dir / "config" / "pipeline.json"

    print("📋 Pipeline Info")
    print("========================")
    print()

    if not config_file.exists():

        print("ℹ️ Pipeline-konfiguraatiota ei löytynyt.")
        return False

    try:

        with config_file.open(
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        for key, value in data.items():

            print(f"{key}: {value}")

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Pipeline-tietojen luku epäonnistui: {e}")

        return False