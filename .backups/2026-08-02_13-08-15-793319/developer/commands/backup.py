from pathlib import Path
import zipfile
from datetime import datetime

from core.logger import log



def command(args):

    if len(args) < 2:

        print(
            "❌ Anna moduulin nimi"
        )

        return False



    if args[0] != "backup":

        return False



    module_name = (
        args[1]
        .strip()
        .lower()
    )


    print(
        "🐻 Module Backup"
    )

    print(
        "========================"
    )


    base = Path(__file__).resolve()


    bearcore = None


    for parent in base.parents:

        if parent.name == "BearCore":

            bearcore = parent

            break



    if not bearcore:

        print(
            "❌ BearCore kansiota ei löytynyt"
        )

        return True



    source = (
        bearcore /
        "modules" /
        module_name
    )


    if not source.exists():

        print(
            f"❌ Moduulia ei löydy: {module_name}"
        )

        return True



    backup_dir = (
        bearcore /
        "backups"
    )


    backup_dir.mkdir(
        exist_ok=True
    )


    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    backup_file = (
        backup_dir /
        f"{module_name}_{timestamp}.zip"
    )



    with zipfile.ZipFile(
        backup_file,
        "w"
    ) as archive:


        for file in source.rglob("*"):

            if file.is_file():

                archive.write(
                    file,
                    file.relative_to(
                        source
                    )
                )



    print(
        "✅ Varmuuskopio luotu:"
    )


    print(
        backup_file
    )


    log(
        f"💾 Backup luotu: {module_name}"
    )


    return True