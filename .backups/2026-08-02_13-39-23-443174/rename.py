from pathlib import Path
import os

from core.module_manager import reload_modules


def command(args=None):

    if args is None:
        args = []

    if len(args) < 3:
        print("Käyttö: rename <vanha_nimi> <uusi_nimi>")
        return False

    if args[0].lower() != "rename":
        return False

    old_name = args[1].strip().lower()
    new_name = args[2].strip().lower()

    modules_dir = Path(__file__).resolve().parent

    old_dir = modules_dir / old_name
    new_dir = modules_dir / new_name

    if not old_dir.exists():
        print(f"❌ Moduulia '{old_name}' ei löytynyt.")
        return False

    if new_dir.exists():
        print(f"❌ Moduuli '{new_name}' on jo olemassa.")
        return False

    print(f"📝 Nimetään '{old_name}' → '{new_name}'...")

    try:

        os.rename(old_dir, new_dir)

        old_py = new_dir / f"{old_name}.py"

        if old_py.exists():

            os.rename(
                old_py,
                new_dir / f"{new_name}.py"
            )

        config = new_dir / "config.json"

        if config.exists():

            data = config.read_text(
                encoding="utf-8"
            )

            data = data.replace(
                f'"name": "{old_name}"',
                f'"name": "{new_name}"'
            )

            config.write_text(
                data,
                encoding="utf-8"
            )

        reload_modules()

        print()
        print(f"✅ Moduuli nimettiin '{new_name}'.")

        return True

    except Exception as e:

        print(f"❌ Virhe nimettäessä moduulia: {e}")

        return False