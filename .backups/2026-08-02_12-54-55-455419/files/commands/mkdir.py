import os


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "mkdir":
        return False

    if len(args) < 2:
        print("Käyttö: files mkdir <kansio>")
        return True

    path = args[1]

    try:

        os.makedirs(path, exist_ok=True)

        print(f"📁 Kansio luotu: {path}")

    except Exception as e:

        print(f"❌ {e}")

    return True