from core.project import project_path


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "cat":
        return False

    if len(args) < 2:
        print("Käyttö: files cat <tiedosto>")
        return True

    filename = project_path(args[1])

    try:

        with open(filename, "r", encoding="utf-8") as file:

            print("")
            print("=" * 60)
            print(filename)
            print("=" * 60)

            print(file.read())
            print("=" * 60)

    except Exception as e:

        print(f"❌ {e}")

    return True