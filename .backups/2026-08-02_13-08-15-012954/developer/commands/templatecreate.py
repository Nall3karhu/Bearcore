import json
from pathlib import Path


def command(args):

    if len(args) < 2:
        return False


    if args[0] != "templatecreate":
        return False


    template_name = args[1].strip().lower()


    current = Path(__file__).resolve()

    base_dir = None


    for parent in current.parents:

        if parent.name == "BearCore":

            base_dir = parent
            break


    if base_dir is None:

        print("❌ BearCore-kansiota ei löytynyt.")
        return True


    template_dir = (
        base_dir /
        "templates" /
        template_name
    )


    if template_dir.exists():

        print(
            f"❌ Template '{template_name}' on jo olemassa."
        )

        return True


    print(
        f"🐻 Luodaan template: {template_name}"
    )


    template_dir.mkdir(
        parents=True
    )


    (template_dir / "__init__.py").write_text(
        "",
        encoding="utf-8"
    )


    config = {
        "name": "",
        "version": "1.0",
        "category": template_name,
        "aliases": [],
        "description": f"{template_name} template"
    }


    with open(
        template_dir / "config.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            config,
            f,
            indent=4,
            ensure_ascii=False
        )


    (template_dir / "template.py").write_text(
        f'''def MODULE_NAME(args=None):

    print("✅ MODULE_NAME {template_name}-moduuli toimii!")
''',
        encoding="utf-8"
    )


    (template_dir / "README.md").write_text(
        f"# {template_name.title()} Template\n\nBearCore template-pohja.",
        encoding="utf-8"
    )


    print("")
    print("✅ Template valmis")

    return True