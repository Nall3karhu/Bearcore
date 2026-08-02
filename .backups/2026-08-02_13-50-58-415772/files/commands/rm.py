import os
import shutil

from core.project import project_path


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "rm":
        return False

    if len(args) < 2:
        print("Käyttö: files rm <kohde>")
        return True

    target = project_path(args[1])

    try:

        if os.path.isdir(target):

            shutil.rmtree(target)

            print(f"📁 Kansio poistettu: {args[1]}")

        else:

            os.remove(target)

            print(f"📄 Tiedosto poistettu: {args[1]}")

    except Exception as e:

        print(f"❌ {e}")

    return True