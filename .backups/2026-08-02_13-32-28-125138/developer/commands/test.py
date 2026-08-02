from core.logger import log


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:

        print("❌ Anna moduulin nimi")
        return False

    if args[0].lower() != "test":

        return False

    module_name = (
        args[1]
        .strip()
        .lower()
    )

    print("🧪 Module Test")
    print("================")

    try:

        __import__(
            f"modules.{module_name}"
        )

        print("✅ Import toimii")
        print("ℹ️ Ei erillistä testitiedostoa.")
        print("-------------------------")
        print("✅ Perustesti läpäisty")

        log(
            f"🧪 Testi onnistui: {module_name}"
        )

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Testi epäonnistui: {e}")

        log(
            f"❌ Testi epäonnistui: {module_name}: {e}"
        )

        return False