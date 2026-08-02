import os
import importlib


SEARCH_PATHS = [

    "commands",
    "module",
    "project",
    "release",
    "doctor",
    "backup"

]


def run_command(args):

    base = os.path.dirname(
        os.path.dirname(__file__)
    )

    command_name = args[0].lower() if args else ""


    # Etsi ensin tarkka komento
    for folder in SEARCH_PATHS:

        folder_path = os.path.join(
            base,
            folder
        )

        if not os.path.exists(folder_path):
            continue


        file_name = f"{command_name}.py"

        if file_name in os.listdir(folder_path):

            try:

                module = importlib.import_module(
                    f"modules.developer.{folder}.{command_name}"
                )

                importlib.reload(module)


                if hasattr(module, "command"):

                    if module.command(args):

                        return True


            except Exception as e:

                print(f"❌ {command_name}: {e}")

                return True


    # Jos tarkkaa tiedostoa ei löydy, käy kaikki läpi
    for folder in SEARCH_PATHS:

        folder_path = os.path.join(
            base,
            folder
        )

        if not os.path.exists(folder_path):
            continue


        for file in os.listdir(folder_path):

            if not file.endswith(".py"):
                continue

            if file == "__init__.py":
                continue


            module_name = file[:-3]


            try:

                module = importlib.import_module(
                    f"modules.developer.{folder}.{module_name}"
                )

                importlib.reload(module)


                if hasattr(module, "command"):

                    if module.command(args):

                        return True


            except Exception as e:

                print(f"❌ {module_name}: {e}")


    return False