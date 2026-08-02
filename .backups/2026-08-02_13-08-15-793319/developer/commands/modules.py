import os


def command(args):

    if not args:
        return False

    if args[0] != "modules":
        return False

    print("📦 BearCore Modules")
    print("-------------------")

    for item in sorted(os.listdir("modules")):

        path = os.path.join("modules", item)

        if os.path.isdir(path):

            print(item)

    return True