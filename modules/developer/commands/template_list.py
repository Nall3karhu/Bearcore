from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "template_list":
        return False

    current = Path(__file__).resolve()

    base_dir = None

    for parent in current.parents:

        if parent.name == "BearCore":

            base_dir = parent
            break

    if base_dir is None:

        print("❌ BearCore-kansiota ei löytynyt.")
        return False

    templates_dir = base_dir / "templates"

    print("📄 BearCore Templates")
    print("====================")

    if not templates_dir.exists():

        print("ℹ️ Templates-kansiota ei löytynyt.")
        return True

    templates = sorted(templates_dir.glob("*"))

    if not templates:

        print("ℹ️ Templateja ei löytynyt.")
        return True

    for template in templates:

        if template.is_dir():

            print(f"📦 {template.name}")

        else:

            print(f"📄 {template.name}")

    return True