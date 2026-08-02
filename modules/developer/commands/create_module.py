import json
from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 3:
        return False

    if args[0].lower() != "create":
        return False

    if args[1].lower() != "module":
        return False

    name = args[2].strip().lower()

    current = Path(__file__).resolve()

    modules_dir = None

    for parent in current.parents:

        if parent.name == "modules":

            modules_dir = parent
            break

    if modules_dir is None:

        print("❌ Modules-kansiota ei löytynyt.")
        return False

    path = modules_dir / name

    if path.exists():

        print(f"❌ Moduuli '{name}' on jo olemassa.")

        return True

    path.mkdir(
        parents=True
    )

    (path / f"{name}.py").write_text(
f'''def {name}(args=None):

    print("✅ {name}-moduuli toimii!")
''',
        encoding="utf-8"
    )

    (path / "__init__.py").write_text(
        "",
        encoding="utf-8"
    )

    with open(
        path / "config.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "name": name,
                "version": "1.0"
            },
            f,
            indent=4,
            ensure_ascii=False
        )

    (path / "README.md").write_text(
        f"# {name}\n\nBearCore Module\n",
        encoding="utf-8"
    )

    print(f"✅ Moduuli '{name}' luotu.")

    return True