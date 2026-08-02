import shutil
from pathlib import Path

from core.module_manager import reload_modules


def command(args):

    if len(args) < 2:
        return False

    if args[0] != "delete":
        return False

    module_name = args[1].strip().lower()

    modules_dir = Path(__file__).resolve().parents[2]
    module_dir = modules_dir / module_name

    if not module_dir.exists():

        print(f"❌ Moduulia '{module_name}' ei löytynyt.")
        return True

    print(f"🗑️ Poistetaan moduuli '{module_name}'...")

    shutil.rmtree(module_dir)

    reload_modules()

    print("")
    print(f"✅ Moduuli '{module_name}' poistettu.")

    return True