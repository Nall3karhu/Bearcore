from core.project import project_path


EXIT_COMMANDS = [
    ":wq",
    ":wq:",
    "save",
    "tallenna",
    "lopeta",
    "exit",
    "quit"
]


def command(args):

    if len(args) == 0:
        return False

    if args[0] != "write":
        return False

    if len(args) < 2:
        print("Käyttö: files write <tiedosto>")
        return True

    filename = project_path(args[1])

    print("")
    print("✍️ BearCore Editor")
    print("")
    print("Kirjoita tekstiä.")
    print("Lopeta kirjoittaminen jollakin seuraavista:")
    print(", ".join(EXIT_COMMANDS))
    print("")

    lines = []

    while True:

        text = input()

        if text.strip().lower() in EXIT_COMMANDS:
            break

        lines.append(text)

    try:

        with open(filename, "w", encoding="utf-8") as file:

            file.write("\n".join(lines))

        print("")
        print("💾 Tallennettu onnistuneesti!")
        print(filename)

    except Exception as e:

        print(f"❌ {e}")

    return True