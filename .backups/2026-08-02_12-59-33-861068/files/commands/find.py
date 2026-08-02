import os

from core.project import PROJECT_ROOT


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "find":
        return False

    if len(args) < 2:
        print("Käyttö: files find <nimi>")
        return True

    keyword = args[1].lower()

    results = []

    for root, dirs, files in os.walk(PROJECT_ROOT):

        for directory in dirs:

            if keyword in directory.lower():

                full = os.path.join(root, directory)

                relative = os.path.relpath(full, PROJECT_ROOT)

                results.append("📁 " + relative)

        for file in files:

            if keyword in file.lower():

                full = os.path.join(root, file)

                relative = os.path.relpath(full, PROJECT_ROOT)

                results.append("📄 " + relative)

    if results:

        print("\n🔍 Löydettiin:\n")

        for result in sorted(results):

            print(result)

    else:

        print("❌ Ei löytynyt.")

    return True