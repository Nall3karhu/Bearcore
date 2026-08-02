import json
from pathlib import Path
from datetime import datetime
import shutil


def command(args):

    if len(args) < 2:
        return False

    if args[0] != "repair":
        return False


    module_name = args[1].strip().lower()


    current = Path(__file__).resolve()

    modules_dir = None
    base_dir = None


    for parent in current.parents:

        if parent.name == "modules":

            modules_dir = parent
            base_dir = parent.parent
            break


    if modules_dir is None:

        print("❌ Modules-kansiota ei löytynyt.")
        return True


    module_dir = modules_dir / module_name


    if not module_dir.exists():

        print(f"❌ Moduulia '{module_name}' ei löytynyt.")
        return True


    print("🐻 Module Repair")
    print(f"🔍 Tarkistetaan: {module_name}")
    print("")


    # Backup ennen muutoksia

    backup_dir = base_dir / "backups"

    backup_dir.mkdir(
        exist_ok=True
    )


    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    backup_name = (
        f"{module_name}_before_repair_{timestamp}"
    )


    shutil.make_archive(
        str(backup_dir / backup_name),
        "zip",
        module_dir
    )


    print("📦 Backup tehty")


    fixes = []


    # __init__.py

    init_file = module_dir / "__init__.py"

    if not init_file.exists():

        init_file.write_text(
            "",
            encoding="utf-8"
        )

        fixes.append(
            "__init__.py luotu"
        )


    # config.json

    config_file = module_dir / "config.json"


    if not config_file.exists():

        config = {

            "name": module_name,
            "version": "1.0",
            "category": "general",
            "aliases": [],
            "description": ""

        }


        config_file.write_text(
            json.dumps(
                config,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )


        fixes.append(
            "config.json luotu"
        )


    print("")
    print("🔧 Korjaukset:")


    if fixes:

        for fix in fixes:

            print(f"✅ {fix}")

    else:

        print("✅ Ei korjattavaa")


    print("")
    print("--------------------------------")
    print("✅ Moduuli tarkistettu")


    return True