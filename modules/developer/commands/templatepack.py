from core.template_engine import create_from_template
from core.logger import log


TEMPLATES = [

    "database_driver",
    "camera",
    "auth",
    "cache",
    "workflow",
    "user",

    "scheduler_task",
    "api_client",
    "hardware_interface",
    "robot_arm",
    "motor",
    "display",
    "power",

    "storage_driver",
    "network_driver",
    "file_manager",

    "notification",
    "email",

    "voice",
    "speech",
    "language",
    "translation",

    "memory",
    "knowledge",
    "search",

    "backup_manager",
    "security_monitor",

    "performance",
    "system",
    "diagnostic",

    "plugin_manager"

]


def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "templatepack":
        return False

    print("📦 Template Pack Generator")
    print("========================")

    created = 0

    try:

        for template in TEMPLATES:

            result = create_from_template(
                template=template,
                module_name=template,
                category=template,
                version="1.0",
                author="BearCore",
                description=f"{template} template"
            )

            if result:

                print(f"✅ Luotu: {template}")
                created += 1

            else:

                print(f"⚠️ On jo olemassa: {template}")

        log(
            f"📦 Template Pack valmis ({created} luotu)"
        )

        print()
        print("✅ Template Pack valmis")

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Template Pack epäonnistui: {e}")

        return False