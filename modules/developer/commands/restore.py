import shutil
from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 2:

        print("❌ Anna backup-tiedoston nimi")
        return False

    if args[0].lower() != "restore":

        return False

    backup_name = args[1].strip()

    current = Path(__file__).resolve()

    base_dir = None

    for parent in current.parents:

        if parent.name == "BearCore":

            base_dir = parent
            break

    if base_dir is None:

        print("❌ BearCore-kansiota ei löytynyt")
        return False

    backup_dir = base_dir / "backups"
    modules_dir = base_dir / "modules"

    backup_file = backup_dir / backup_name

    if not backup_file.exists():

        print(f"❌ Backupia ei löytynyt: {backup_name}")
        return False

    print("📦 Module Restore")
    print("================")
    print(f"Palautetaan: {backup_file.name}")

    try:

        shutil.unpack_archive(
            str(backup_file),
            str(modules_dir)
        )

        print("✅ Palautus onnistui")

        return True

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Palautus epäonnistui: {e}")

        return False