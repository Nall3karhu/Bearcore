import os


def files(args=None):

    if args is None:
        args = []

    if len(args) == 0:
        print("""
=========================
BearCore File Manager
=========================

Komennot:

files list
files read <tiedosto>
files find <hakusana>
""")
        return

    # -------------------------
    # Listaa tiedostot
    # -------------------------

    if args[0] == "list":

        print("\n📁 Projektin tiedostot:\n")

        for root, dirs, files_list in os.walk("."):

            dirs[:] = [d for d in dirs if d not in (
                "__pycache__",
                ".git",
                ".venv",
                "venv"
            )]

            level = root.count(os.sep)

            indent = "    " * level

            print(f"{indent}{os.path.basename(root)}/")

            subindent = "    " * (level + 1)

            for file in files_list:
                print(f"{subindent}{file}")

        return

    # -------------------------
    # Lue tiedosto
    # -------------------------

    if args[0] == "read":

        if len(args) < 2:
            print("Käyttö: files read <tiedosto>")
            return

        filename = " ".join(args[1:])

        if not os.path.exists(filename):
            print("❌ Tiedostoa ei löytynyt.")
            return

        try:

            with open(filename, "r", encoding="utf-8") as f:

                print("\n=========================\n")

                print(f.read())

        except Exception as e:

            print(e)

        return

    # -------------------------
    # Etsi tiedosto
    # -------------------------

    if args[0] == "find":

        if len(args) < 2:
            print("Käyttö: files find <hakusana>")
            return

        word = " ".join(args[1:]).lower()

        print(f"\n🔍 Haetaan '{word}'...\n")

        found = False

        for root, dirs, files_list in os.walk("."):

            dirs[:] = [d for d in dirs if d not in (
                "__pycache__",
                ".git",
                ".venv",
                "venv"
            )]

            for file in files_list:

                if word in file.lower():

                    print(os.path.join(root, file))

                    found = True

        if not found:
            print("Ei löytynyt.")

        return

    print("Tuntematon files-komento.")
