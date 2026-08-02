from core.logger import log



def command(args):


    if len(args) < 2:

        print(
            "❌ Anna moduulin nimi"
        )

        return False



    if args[0] != "test":

        return False



    module_name = (
        args[1]
        .strip()
        .lower()
    )


    print(
        "🐻 Module Test"
    )

    print(
        "================"
    )


    try:


        __import__(
            f"modules.{module_name}"
        )


        print(
            "✅ Import toimii"
        )


        print(
            "ℹ️ Ei testitiedostoa."
        )


        print(
            "-------------------------"
        )


        print(
            "✅ Perustesti läpäisty"
        )


        log(
            f"🧪 Testi onnistui: {module_name}"
        )


        return True



    except Exception as e:


        print(
            "❌ Testi epäonnistui"
        )


        print(
            e
        )


        log(
            f"❌ Testi epäonnistui: {module_name}"
        )


        return False