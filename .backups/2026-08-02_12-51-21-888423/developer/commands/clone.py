import json
import shutil
from pathlib import Path

from core.module_manager import reload_modules


def command(args):

    if len(args) < 3:
        return False

    if args[0] != "clone":
        return False

    source_name = args[1].strip().lower()
    target_name = args[2].strip().lower()

    modules_dir = Path(__file__).resolve().parents[2]

    source_dir = modules_dir / source_name
    target_dir = modules_dir / target_name

    if not source_dir.exists():

        print(f"❌ Moduulia '{source_name}' ei löytynyt.")
        return True

    if target_dir.exists():

        print(f"❌ Moduuli '{target_name}' on jo olemassa.")
        return True

    print(f"📋 Kloonataan '{source_name}' -> '{target_name}'...")

    shutil.copytree(
        source_dir,
        target_dir
    )

    # Python tiedoston nimi
    old_py = target_dir / f"{source_name}.py"
    new_py = target_dir / f"{target_name}.py"

    if old_py.exists():

        old_py.rename(new_py)

    # Päivitä python sisältö
    if new_py.exists():

        text = new_py.read_text(
            encoding="utf-8"
        )

        text = text.replace(
            source_name,
            target_name
        )

        new_py.write_text(
            text,
            encoding="utf-8"
        )


    # Päivitä config
    config = target_dir / "config.json"

    if config.exists():

        with open(config, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["name"] = target_name

        with open(config, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


    reload_modules()

    print("")
    print(f"✅ Moduuli '{target_name}' luotu kopioksi.")

    return True