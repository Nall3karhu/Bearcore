import os
from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "modules":
        return False

    modules_dir = Path(__file__).resolve().parents[2]

    print("📦 BearCore Modules")
    print("-------------------")

    if not modules_dir.exists():

        print("❌ Modules-kansiota ei löytynyt.")
        return False

    for item in sorted(os.listdir(modules_dir)):

        path = modules_dir / item

        if path.is_dir():

            print(item)

    return True