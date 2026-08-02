from pathlib import Path

from core.module_manager import reload_modules
from core.template_engine import create_from_template


def command(args):

    if len(args) < 2:
        return False

    if args[0] != "create":
        return False

    module_name = args[1].strip().lower()

    template = "empty"

    if len(args) >= 3:
        template = args[2].strip().lower()

    modules_dir = Path(__file__).resolve().parents[2]
    module_dir = modules_dir / module_name

    if module_dir.exists():

        print(f"❌ Moduuli '{module_name}' on jo olemassa.")
        return True

    print(f"🛠️ Luodaan moduuli '{module_name}'...")
    print(f"📦 Template: {template}")

    if not create_from_template(

        template=template,
        module_name=module_name,
        category=template,
        version="1.0",
        author="BearCore",
        description=""

    ):

        return True

    reload_modules()

    print("")
    print(f"✅ Moduuli '{module_name}' valmis.")
    print("🚀 Voit käyttää sitä heti.")

    return True