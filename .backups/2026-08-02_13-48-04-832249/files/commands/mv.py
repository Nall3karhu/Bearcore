import shutil

from core.project import project_path


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "mv":
        return False

    if len(args) < 3:
        print("Käyttö: files mv <lähde> <kohde>")
        return True

    source = project_path(args[1])
    target = project_path(args[2])

    try:

        shutil.move(source, target)

        print(f"📦 Siirretty:\n{args[1]} -> {args[2]}")

    except Exception as e:

        print(f"❌ {e}")

    return True