import importlib
from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:
        print("Käyttö: developer validate <moduuli>")
        return False

    if args[0].lower() != "validate":
        return False

    module_name = args[1].strip().lower()

    current = Path(__file__).resolve()

    modules_dir = None

    for parent in current.parents:

        if parent.name == "modules":
            modules_dir = parent
            break

    if modules_dir is None:
        print("❌ Modules-kansiota ei löytynyt.")
        return False

    module_dir = modules_dir / module_name

    print("🔍 Module Validator")
    print(f"Tarkistetaan: {module_name}")
    print()

    errors = []

    if module_dir.exists():
        print("✅ Moduulikansio löytyy")
    else:
        errors.append("Moduulikansiota ei löydy")

    py_file = module_dir / f"{module_name}.py"

    if py_file.exists():
        print("✅ Python-tiedosto löytyy")
    else:
        errors.append("Python-tiedosto puuttuu")

    init_file = module_dir / "__init__.py"

    if init_file.exists():
        print("✅ __init__.py löytyy")
    else:
        errors.append("__init__.py puuttuu")

    config_file = module_dir / "config.json"

    if config_file.exists():
        print("✅ config.json löytyy")
    else:
        errors.append("config.json puuttuu")

    if py_file.exists():

        try:

            module = importlib.import_module(
                f"modules.{module_name}.{module_name}"
            )

            if hasattr(module, module_name):
                print("✅ Moduulifunktio löytyy")
            else:
                errors.append("Moduulifunktio puuttuu")

        except Exception as e:

            errors.append(f"Import-virhe: {e}")

    print()

    if errors:

        print("❌ Löydetyt ongelmat:")

        for error in errors:
            print(f" - {error}")

        return False

    print("✅ Moduuli läpäisi kaikki tarkistukset.")

    return True