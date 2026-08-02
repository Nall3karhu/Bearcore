import json
from pathlib import Path


def command(args):

    if not args:
        return False

    if args[0] != "pinfo":
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


    config_file = (
        base_dir /
        "config" /
        "pipeline.json"
    )


    print("🐻 Pipeline Info")
    print("========================")
    print("")


    if not config_file.exists():

        print("❌ pipeline.json puuttuu.")
        return True


    with open(
        config_file,
        "r",
        encoding="utf-8"
    ) as f:

        config = json.load(f)


    print("📦 Vaiheet:")

    for step in config.get("steps", []):

        print(f"✅ {step}")


    print("")
    print("📄 Config:")
    print("config/pipeline.json")


    return True