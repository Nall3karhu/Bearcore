import os

from core.project import PROJECT_ROOT


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "grep":
        return False

    if len(args) < 2:
        print("Käyttö: files grep <teksti>")
        return True

    keyword = " ".join(args[1:]).lower()

    found = False

    print(f"\n🔍 Haetaan: '{keyword}'\n")

    for root, _, files in os.walk(PROJECT_ROOT):

        for file in files:

            if not file.endswith(".py"):
                continue

            full_path = os.path.join(root, file)

            try:

                with open(full_path, "r", encoding="utf-8") as f:

                    for number, line in enumerate(f, start=1):

                        if keyword in line.lower():

                            relative = os.path.relpath(
                                full_path,
                                PROJECT_ROOT
                            )

                            print(
                                f"📄 {relative}:{number}\n"
                                f"    {line.strip()}"
                            )

                            found = True

            except Exception:
                pass

    if not found:

        print("❌ Ei osumia.")

    return True