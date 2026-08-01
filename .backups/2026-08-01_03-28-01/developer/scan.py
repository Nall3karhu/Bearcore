import os


def scan_project(args=None):

    print("\n🐻 BearCore Project Scan")
    print("=" * 35)

    modules = []
    python_files = 0
    folders = 0

    for root, dirs, files in os.walk("."):

        folders += len(dirs)

        for file in files:

            if file.endswith(".py"):

                python_files += 1

                if "modules" in root:

                    parts = root.split(os.sep)

                    if "modules" in parts:

                        index = parts.index("modules")

                        if len(parts) > index + 1:

                            module = parts[index + 1]

                            if module not in modules:
                                modules.append(module)


    print(f"\n📁 Kansioita: {folders}")
    print(f"🐍 Python tiedostoja: {python_files}")

    print("\n🔌 Moduulit:")

    if modules:

        for module in sorted(modules):
            print(f"✅ {module}")

    else:

        print("Ei moduuleita löytynyt.")


    print("\n🟢 Skannaus valmis.")