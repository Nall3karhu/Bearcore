from pathlib import Path

from core.project import project_path


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "list":
        return False

    template_dir = Path(project_path("templates"))

    print("")
    print("=== Templatet ===")
    print("")

    for folder in sorted(template_dir.iterdir()):

        if folder.is_dir():

            print(f"- {folder.name}")

    return True