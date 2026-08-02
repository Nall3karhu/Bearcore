from core.template_engine import create_from_template
from core.module_manager import reload_modules
from core.logger import log



def command(args):

    if len(args) < 2:

        print(
            "❌ Anna moduulin nimi"
        )

        return False



    if args[0] != "create":

        return False



    module_name = (
        args[1]
        .strip()
        .lower()
    )


    template = "empty"


    if len(args) >= 3:

        template = (
            args[2]
            .strip()
            .lower()
        )



    print(
        "🐻 Module Creator"
    )

    print(
        "================"
    )


    result = create_from_template(

        template=template,

        module_name=module_name,

        category=template,

        version="1.0",

        author="BearCore",

        description="BearCore moduuli"

    )


    if not result:

        print(
            "❌ Moduulin luonti epäonnistui"
        )


        log(
            f"❌ Moduulin luonti epäonnistui: {module_name}"
        )


        return True



    reload_modules()


    print(
        f"✅ Luotu: {module_name}"
    )


    log(
        f"➕ Moduuli luotu: {module_name}"
    )


    return True