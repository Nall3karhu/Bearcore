import os
import importlib


def run_command(args):

    folder = os.path.dirname(__file__)

    for file in os.listdir(folder):

        if not file.endswith(".py"):
            continue

        if file in [
            "__init__.py",
            "loader.py"
        ]:
            continue

        module_name = file[:-3]

        try:

            module = importlib.import_module(
                f"modules.files.commands.{module_name}"
            )

            importlib.reload(module)

            if hasattr(module, "command"):

                result = module.command(args)

                if result:
                    return True

        except Exception as e:

            print(f"❌ Virhe files-komennossa {module_name}: {e}")

    return False