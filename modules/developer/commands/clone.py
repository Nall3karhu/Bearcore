import json
import shutil
from pathlib import Path

from core.module_manager import reload_modules


def command(args=None):

    if args is None:
        args = []

    if len(args) < 3:
        print("❌ Käyttö: clone <lähde> <kohde>")
        return False

    if args[0].lower() != "clone":
        return False

    source_name = args[1].strip().lower()
    target_name = args[2].strip().lower()

    modules_dir = Path(__file__).resolve().parents[2]

    source_dir = modules_dir / source_name
    target_dir = modules_dir / target_name

    if not source_dir.exists():

        print(f"❌ Moduulia '{source_name}' ei löytynyt.")
        return False

    if target_dir.exists():

        print(f"❌ Moduuli '{target_name}' on jo olemassa.")
        return False

    print(f"📋 Kloonataan '{source_name}' -> '{target_name}'...")

    try:

        shutil.copytree(
            source_dir,
            target_dir
        )

        old_py = target_dir / f"{source_name}.py"
        new_py = target_dir / f"{target_name}.py"

        if old_py.exists():

            old_py.rename(new_py)

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

        config = target_dir / "config.json"

        if config.exists():

            with config.open(
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

            data["name"] = target_name

            with config.open(
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    data,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

        reload_modules()

        print()
        print(f"✅ Moduuli '{target_name}' luotu kopioksi.")

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Kloonaus epäonnistui: {e}")

        return False