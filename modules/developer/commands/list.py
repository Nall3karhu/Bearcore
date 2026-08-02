from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "list":
        return False

    current = Path(__file__).resolve()

    commands_dir = None

    for parent in current.parents:

        if parent.name == "commands":

            commands_dir = parent
            break

    if commands_dir is None:

        print("❌ Commands-kansiota ei löytynyt.")
        return False

    commands = sorted(
        file.stem
        for file in commands_dir.glob("*.py")
        if file.name != "__init__.py"
    )

    print("📋 Developer Commands")
    print("--------------------------------")

    for cmd in commands:

        print(f"✅ {cmd}")

    print("--------------------------------")
    print(f"Yhteensä: {len(commands)} komentoa")

    return True