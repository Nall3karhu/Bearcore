import shutil
from pathlib import Path


def command(args):

    if len(args) < 2:
        return False

    if args[0] != "restore":
        return False


    backup_name = args[1].strip()


    current = Path(__file__).resolve()

    base_dir = None

    for parent in current.parents:

        if parent.name == "BearCore":

            base_dir = parent
            break


    if base_dir is None:

        print("❌ BearCore-kansiota ei löytynyt.")
        return True


    backup_dir = base_dir / "backups"
    modules_dir = base_dir / "modules"


    backup_file = backup_dir / backup_name


    if not backup_file.exists():

        # kokeillaan ilman .zip päätettä
        backup_file = backup_dir / f"{backup_name}.zip"


    if not backup_file.exists():

        print(
            f"❌ Varmuuskopiota '{backup_name}' ei löytynyt."
        )

        return True


    print("🐻 Module Restore")
    print(f"📦 Palautetaan: {backup_file.name}")


    try:

        shutil.unpack_archive(
            str(backup_file),
            str(modules_dir)
        )


    except Exception as e:

        print(
            f"❌ Palautus epäonnistui: {e}"
        )

        return True


    print("")
    print("✅ Moduuli palautettu.")

    return True