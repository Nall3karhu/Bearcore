from pathlib import Path


def command(args):

    if len(args) < 1:
        return False

    if args[0] != "list":
        return False


    current = Path(__file__).resolve()

    commands_dir = None


    for parent in current.parents:

        if parent.name == "commands":

            commands_dir = parent
            break


    if commands_dir is None:

        print("❌ Commands-kansiota ei löytynyt.")
        return True


    commands = []


    for file in commands_dir.iterdir():

        if not file.name.endswith(".py"):
            continue

        if file.name == "__init__.py":
            continue

        commands.append(
            file.stem
        )


    commands.sort()


    print("🐻 Developer Commands")
    print("--------------------------------")


    for cmd in commands:

        print(
            f"✅ {cmd}"
        )


    print("--------------------------------")
    print(
        f"Yhteensä: {len(commands)} komentoa"
    )


    return True