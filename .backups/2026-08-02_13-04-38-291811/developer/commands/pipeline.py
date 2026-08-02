import json
from pathlib import Path


from core.template_engine import create_from_template
from core.module_manager import reload_modules

from modules.developer.commands.test import command as test_command
from modules.developer.commands.backup import command as backup_command
from modules.developer.commands.deploy import command as deploy_command

from core.logger import log



def command(args):


    if len(args) < 2:

        return False



    if args[0] != "pipeline":

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
        "🐻 Developer Pipeline"
    )

    print(
        "================================"
    )


    print(
        f"📦 Moduuli: {module_name}"
    )

    print(
        f"📦 Template: {template}"
    )


    print()



    result = create_from_template(

        template=template,

        module_name=module_name,

        category=template,

        version="1.0",

        author="BearCore",

        description="Pipeline luoma moduuli"

    )


    if not result:

        print(
            "❌ Build epäonnistui"
        )

        log(
            f"❌ Pipeline epäonnistui: {module_name}"
        )

        return True



    reload_modules()


    print(
        "✅ Build valmis"
    )


    test_command(
        [
            "test",
            module_name
        ]
    )


    backup_command(
        [
            "backup",
            module_name
        ]
    )


    deploy_command(
        [
            "deploy",
            module_name
        ]
    )



    log(
        f"🚀 Pipeline valmis: {module_name}"
    )


    print(
        "--------------------------------"
    )


    print(
        "🚀 Pipeline valmis"
    )


    return True