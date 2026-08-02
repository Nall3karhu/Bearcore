import os


def show_tree(path, indent=""):

    items = sorted(os.listdir(path))

    for item in items:

        full = os.path.join(path, item)

        if os.path.isdir(full):

            print(f"{indent}📁 {item}")

            show_tree(full, indent + "    ")

        else:

            print(f"{indent}📄 {item}")


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "tree":
        return False

    path = "."

    if len(args) >= 2:
        path = args[1]

    try:

        print(f"\n🌳 {os.path.abspath(path)}")

        show_tree(path)

    except Exception as e:

        print(f"❌ {e}")

    return True