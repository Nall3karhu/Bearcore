from pathlib import Path

from core.module_manager import reload_modules
from core.template_engine import create_from_template


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:
        print("Käyttö: create <moduuli> [template]")
        return False

    if args[0].lower() != "create":
        return False

    module_name = args[1].strip().lower()

    template = "empty"

    if len(args) >= 3:
        template = args[2].strip().lower()

    modules_dir = Path(__file__).resolve().parent
    module_dir = modules_dir / module_name

    if module_dir.exists():
        print(f"❌ Moduuli '{module_name}' on jo olemassa.")
        return False

    print(f"📦 Luodaan moduuli '{module_name}'...")
    print(f"📄 Template: {template}")

    success = create_from_template(
        template=template,
        module_name=module_name,
        category=template,
        version="1.0",
        author="BearCore",
        description=""
    )

    if not success:
        print("❌ Moduulin luonti epäonnistui.")
        return False

    reload_modules()

    print()
    print(f"✅ Moduuli '{module_name}' valmis.")
    print("🚀 Voit käyttää sitä heti.")

    return True