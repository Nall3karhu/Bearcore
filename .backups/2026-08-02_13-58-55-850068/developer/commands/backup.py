from pathlib import Path
import zipfile
from datetime import datetime

from core.logger import log


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:

        print("❌ Anna moduulin nimi")
        return False

    if args[0].lower() != "backup":

        return False

    module_name = (
        args[1]
        .strip()
        .lower()
    )

    print("🐻 Module Backup")
    print("========================")

    base = Path(__file__).resolve()

    bearcore = None

    for parent in base.parents:

        if parent.name == "BearCore":

            bearcore = parent
            break

    if bearcore is None:

        print("❌ BearCore-kansiota ei löytynyt")
        return False

    source = (
        bearcore /
        "modules" /
        module_name
    )

    if not source.exists():

        print(f"❌ Moduulia ei löydy: {module_name}")
        return False

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

    try:

        with zipfile.ZipFile(
            backup_file,
            "w",
            zipfile.ZIP_DEFLATED
        ) as archive:

            for file in source.rglob("*"):

                if file.is_file():

                    archive.write(
                        file,
                        file.relative_to(source)
                    )

        print("✅ Varmuuskopio luotu:")
        print(backup_file)

        log(
            f"💾 Backup luotu: {module_name}"
        )

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Backup epäonnistui: {e}")

        return False