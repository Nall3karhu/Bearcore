import os


def create_command(name):

    name = name.lower()


    path = os.path.join(
        "modules",
        "developer",
        "commands",
        f"{name}.py"
    )


    if os.path.exists(path):

        print("❌ Komento on jo olemassa.")
        return


    code = f'''def command(args):

    if args[0] == "{name}":

        print("🐻 BearCore {name} toimii.")

        return True


    return False
'''


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(code)


    print("\n🐻 Plugin Creator")
    print("===================")

    print(f"✅ Luotu komento: {name}")
    print(f"📄 {path}")