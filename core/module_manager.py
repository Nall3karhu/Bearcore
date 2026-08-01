import importlib
import json
from pathlib import Path

from core.module_registry import register

MODULES = {}

BASE_DIR = Path(__file__).resolve().parent.parent
MODULES_PATH = BASE_DIR / "modules"


def load_modules():

    MODULES.clear()

    if not MODULES_PATH.exists():
        return

    for folder in MODULES_PATH.iterdir():

        if not folder.is_dir():
            continue

        module_name = folder.name
        py_file = folder / f"{module_name}.py"

        if not py_file.exists():
            continue

        try:

            module = importlib.import_module(
                f"modules.{module_name}.{module_name}"
            )

            importlib.reload(module)

            if not hasattr(module, module_name):
                continue

            function = getattr(module, module_name)

            # Rekisteröidään moduulin komento
            MODULES[module_name] = function

            config = {}

            config_file = folder / "config.json"

            if config_file.exists():

                with open(
                    config_file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    config = json.load(f)

            # Rekisteröidään moduuli Registryyn
            register(

                module_name,

                {

                    "name": module_name,
                    "version": config.get("version", "1.0"),
                    "aliases": config.get("aliases", []),
                    "description": config.get("description", ""),
                    "category": config.get("category", "general")

                }

            )

            # Rekisteröidään alias-komennot
            for alias in config.get("aliases", []):

                MODULES[alias] = function

        except Exception as e:

            print(f"❌ {module_name}: {e}")


def reload_modules():

    print("♻️ Päivitetään moduulit...")

    load_modules()

    print(f"✅ {len(MODULES)} moduulia ladattu.")


def run_module(command):

    if len(MODULES) == 0:
        load_modules()

    parts = command.split()

    if len(parts) == 0:
        return False

    module_name = parts[0]

    if module_name not in MODULES:
        return False

    args = parts[1:]

    MODULES[module_name](args)

    return True