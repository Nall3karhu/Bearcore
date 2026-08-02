import os

from core.project import project_path


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "touch":
        return False

    if len(args) < 2:
        print("Käyttö: files touch <tiedosto>")
        return True

    filename = project_path(args[1])

    try:

        folder = os.path.dirname(filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(filename, "a", encoding="utf-8"):
            pass

        print(f"📄 Tiedosto luotu: {filename}")

    except Exception as e:

        print(f"❌ {e}")

    return True