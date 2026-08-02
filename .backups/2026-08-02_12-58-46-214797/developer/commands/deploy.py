from pathlib import Path

from core.logger import log



def command(args):


    if len(args) < 2:

        print(
            "❌ Anna moduulin nimi"
        )

        return False



    if args[0] != "deploy":

        return False



    module_name = (
        args[1]
        .strip()
        .lower()
    )


    print(
        "🚀 Module Deploy"
    )

    print(
        "================"
    )



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



    if not module or not module.exists():

        print(
            "❌ Moduulia ei löydy"
        )


        log(
            f"❌ Deploy epäonnistui: {module_name}"
        )


        return True



    print(
        f"✅ Deploy valmis: {module_name}"
    )


    log(
        f"🚀 Deploy valmis: {module_name}"
    )


    return True