import os
import json


def create_module(args):

    if len(args) == 0:
        print("Käyttö: developer new module <nimi>")
        return

    name = args[0].lower()

    path = os.path.join("modules", name)

    if os.path.exists(path):
        print(f"❌ Moduuli {name} on jo olemassa.")
        return

    os.makedirs(path)
    os.makedirs("docs", exist_ok=True)
    os.makedirs("tests", exist_ok=True)

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
        "w"
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

        f.write(f"# {name}\n\nBearCore moduuli.\n")

    with open(
        os.path.join("tests", f"test_{name}.py"),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
f'''from modules.{name}.{name} import {name}


def test_{name}():

    {name}()
'''
        )

    with open(
        os.path.join("docs", f"{name}.md"),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(f"# {name}\n")

    print(f"✅ Luotu moduuli: {name}")