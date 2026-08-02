import os
import ast


def module_validator(args=None):
    print("🐻 Module Validator käynnissä")

    # Perustesti ilman moduulia
    if not args:
        print("✅ Ei tarkistettavaa moduulia - perustoiminta OK")
        return True

    module_name = args[0] if isinstance(args, list) else args

    module_path = os.path.join(
        "modules",
        module_name
    )

    print(f"🔍 Tarkistetaan: {module_name}")

    errors = []

    if not os.path.exists(module_path):
        errors.append("Moduulikansiota ei löydy")

    else:
        py_files = [
            f for f in os.listdir(module_path)
            if f.endswith(".py")
        ]

        if not py_files:
            errors.append("Python-tiedosto puuttuu")

        if not os.path.exists(
            os.path.join(module_path, "__init__.py")
        ):
            errors.append("__init__.py puuttuu")

        for file in py_files:

            # __init__.py ei tarvitse sisältää funktioita
            if file == "__init__.py":
                continue

            filepath = os.path.join(
                module_path,
                file
            )

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read())

                functions = [
                    node.name
                    for node in ast.walk(tree)
                    if isinstance(node, ast.FunctionDef)
                ]

                if not functions:
                    errors.append(
                        f"{file}: ei funktioita"
                    )

            except Exception as e:
                errors.append(
                    f"{file}: {e}"
                )

    if errors:
        print("❌ Virheitä:")

        for error in errors:
            print("-", error)

        return False

    print("✅ Moduuli hyväksytty")
    return True