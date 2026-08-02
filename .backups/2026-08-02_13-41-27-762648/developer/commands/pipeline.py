from core.template_engine import create_from_template
from core.module_manager import reload_modules

from modules.developer.commands.test import command as test_command
from modules.developer.commands.backup import command as backup_command
from modules.developer.commands.deploy import command as deploy_command

from core.logger import log


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:
        print("Käyttö: developer pipeline <moduuli> [template]")
        return False

    if args[0].lower() != "pipeline":
        return False

    module_name = args[1].strip().lower()

    template = "empty"

    if len(args) >= 3:
        template = args[2].strip().lower()

    print("🚀 Developer Pipeline")
    print("================================")
    print(f"📦 Moduuli: {module_name}")
    print(f"📄 Template: {template}")
    print()

    try:

        result = create_from_template(
            template=template,
            module_name=module_name,
            category=template,
            version="1.0",
            author="BearCore",
            description="Pipeline luoma moduuli",
        )

        if not result:
            print("❌ Moduulin luonti epäonnistui.")
            return False

        reload_modules()

        print("💾 Luodaan varmuuskopio...")
        backup_command(["backup", module_name])

        print("🧪 Ajetaan testit...")
        test_command(["test", module_name])

        print("🚀 Suoritetaan deploy...")
        deploy_command(["deploy", module_name])

        log(f"Pipeline valmis: {module_name}")

        print()
        print("================================")
        print(f"✅ Pipeline valmis: {module_name}")

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Pipeline epäonnistui: {e}")

        return False