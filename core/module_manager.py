import importlib
import os

MODULES = {}


def load_modules():

    MODULES.clear()

    modules_path = "modules"

    if not os.path.exists(modules_path):
        return

    for folder in os.listdir(modules_path):

        folder_path = os.path.join(modules_path, folder)

        if not os.path.isdir(folder_path):
            continue

        py_file = os.path.join(folder_path, f"{folder}.py")

        if not os.path.exists(py_file):
            continue

        try:

            module = importlib.import_module(f"modules.{folder}.{folder}")

            if hasattr(module, folder):

                MODULES[folder] = getattr(module, folder)

                print(f"✅ Ladattu moduuli: {folder}")

        except Exception as e:

            print(f"❌ Virhe moduulissa {folder}: {e}")


def run_module(command):

    if len(MODULES) == 0:
        load_modules()

    parts = command.split()

    if len(parts) == 0:
        return False

    module = parts[0]

    if module in MODULES:

        args = parts[1:]

        MODULES[module](args)

        return True

    return False