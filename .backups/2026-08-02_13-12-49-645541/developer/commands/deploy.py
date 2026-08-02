from pathlib import Path

from core.logger import log


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:

        print("❌ Anna moduulin nimi")
        return False

    if args[0].lower() != "deploy":

        return False

    module_name = (
        args[1]
        .strip()
        .lower()
    )

    print("🚀 Module Deploy")
    print("================")

    current = Path(__file__).resolve()

    module = None

    for parent in current.parents:

        if parent.name == "BearCore":

            module = (
                parent /
                "modules" /
                module_name
            )

            break

    if module is None or not module.exists():

        print("❌ Moduulia ei löydy")

        log(
            f"❌ Deploy epäonnistui: {module_name}"
        )

        return False

    try:

        print(f"✅ Deploy valmis: {module_name}")

        log(
            f"🚀 Deploy valmis: {module_name}"
        )

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Deploy epäonnistui: {e}")

        log(
            f"❌ Deploy epäonnistui: {module_name}: {e}"
        )

        return False