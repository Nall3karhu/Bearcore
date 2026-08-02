from pathlib import Path

from core.module_manager import reload_modules
from core.template_engine import create_from_template


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:
        print("Käyttö: developer build <moduuli> [template]")
        return False

    if args[0].lower() != "build":
        return False

    module_name = args[1].strip().lower()

    template = "empty"

    if len(args) >= 3:
        template = args[2].strip().lower()

    modules_dir = Path(__file__).resolve().parents[2]
    module_dir = modules_dir / module_name

    if module_dir.exists():
        print(f"❌ Moduuli '{module_name}' on jo olemassa.")
        return False

    print(f"🔨 Developer Build: {module_name}")
    print(f"📦 Template: {template}")

    try:

        result = create_from_template(
            template=template,
            module_name=module_name,
            category="developer",
            version="1.0",
            author="BearCore",
            description="Luotu developer build -komennolla",
        )

        if not result:
            print("❌ Moduulin luonti epäonnistui.")
            return False

        reload_modules()

        print()
        print(f"✅ Moduuli '{module_name}' rakennettu onnistuneesti.")

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Developer Build epäonnistui: {e}")

        return False