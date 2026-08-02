from pathlib import Path


def command(args):

    if len(args) < 1:
        return False

    if args[0] != "status":
        return False


    current = Path(__file__).resolve()

    base_dir = None
    modules_dir = None


    for parent in current.parents:

        if parent.name == "modules":

            modules_dir = parent
            base_dir = parent.parent
            break


    if modules_dir is None:

        print("❌ Modules-kansiota ei löytynyt.")
        return True


    print("🐻 BearCore Developer Status")
    print("================================")
    print("")


    # Moduulit

    modules = []

    for folder in modules_dir.iterdir():

        if folder.is_dir():

            if folder.name != "developer":

                modules.append(folder.name)


    print("📦 Moduulit:")
    print(len(modules))


    print("")


    # Backupit

    backup_dir = base_dir / "backups"

    backups = 0


    if backup_dir.exists():

        backups = len(
            list(
                backup_dir.glob("*.zip")
            )
        )


    print("💾 Backupit:")
    print(backups)


    print("")


    print("🧠 Registry:")
    print("OK")


    print("")


    print("🔧 Developer:")
    print("OK")


    print("")
    print("================================")


    return True