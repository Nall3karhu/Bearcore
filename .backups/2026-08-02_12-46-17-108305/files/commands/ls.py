import os


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "ls":
        return False

    path = "."

    if len(args) >= 2:
        path = args[1]

    try:

        print("")

        for item in sorted(os.listdir(path)):

            full = os.path.join(path, item)

            if os.path.isdir(full):
                print(f"📁 {item}")
            else:
                print(f"📄 {item}")

    except Exception as e:

        print(f"❌ {e}")

    return True