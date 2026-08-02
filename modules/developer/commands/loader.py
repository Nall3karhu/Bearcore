from pathlib import Path
import importlib


SEARCH_PATHS = [
    "commands",
    "module",
    "project",
    "release",
    "doctor",
    "backup",
]


def run_command(args=None):

    if args is None:
        args = []

    if not args:
        return False

    base = Path(__file__).resolve().parent.parent

    command_name = args[0].lower()

    # Etsi ensin tarkka komento
    for folder in SEARCH_PATHS:

        folder_path = base / folder

        if not folder_path.exists():
            continue

        file_name = f"{command_name}.py"

        if (folder_path / file_name).exists():

            try:

                module = importlib.import_module(
                    f"modules.developer.{folder}.{command_name}"
                )

                importlib.reload(module)

                if hasattr(module, "command"):

                    return bool(module.command(args))

            except KeyboardInterrupt:
                raise

            except Exception as e:

                print(
                    f"❌ Virhe ladattaessa developer-komentoa "
                    f"'{command_name}': {e}"
                )

                return False

    print(f"❌ Developer-komentoa '{command_name}' ei löytynyt.")

    return False