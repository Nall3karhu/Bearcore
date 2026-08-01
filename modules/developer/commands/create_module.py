import json
import os


def command(args):

    if len(args) < 3:
        return False

    if args[0] != "create":
        return False

    if args[1] != "module":
        return False

    name = args[2].lower()

    path = os.path.join("modules", name)

    if os.path.exists(path):
        print(f"❌ Moduuli '{name}' on jo olemassa.")
        return True

    os.makedirs(path)

    with open(
        os.path.join(path, f"{name}.py"),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
f'''def {name}(args=None):

    print("✅ {name}-moduuli toimii!")
'''
        )

    open(
        os.path.join(path, "__init__.py"),
        "w",
        encoding="utf-8"
    ).close()

    with open(
        os.path.join(path, "config.json"),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "name": name,
                "version": "1.0"
            },
            f,
            indent=4
        )

    with open(
        os.path.join(path, "README.md"),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(f"# {name}\n\nBearCore Module\n")

    os.makedirs("tests", exist_ok=True)

    with open(
        os.path.join("tests", f"test_{name}.py"),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
f'''from modules.{name}.{name} import {name}


def test_{name}():

    assert {name}() is None
'''
        )

    print(f"✅ Moduuli '{name}' luotu.")

    return True