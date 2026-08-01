from core.memory import (
    save_memory,
    load_memory,
    list_memories
)

from core.module_manager import (
    run_module,
    MODULES
)

from core.smart_command import suggest


COMMANDS = [

    "apu",
    "moduulit",
    "muista",
    "hae",
    "listaa",
    "files",
    "developer",
    "brain",
    "knowledge",
    "lopeta"

]


def handle_command(command):

    osat = command.strip().split()

    if len(osat) == 0:
        return True

    # -------------------------
    # APU
    # -------------------------

    if osat[0] == "apu":

        print("""
Komennot:

apu
moduulit

muista <avain> <tieto>
hae <avain>
listaa

files
developer
brain

lopeta
""")

        return True

    # -------------------------
    # MODUULIT
    # -------------------------

    if osat[0] == "moduulit":

        print("\n=== Ladatut moduulit ===\n")

        for nimi in sorted(MODULES.keys()):
            print(f"- {nimi}")

        return True

    # -------------------------
    # MUISTI
    # -------------------------

    if osat[0] == "muista":

        if len(osat) < 3:

            print("Käyttö:")
            print("muista <avain> <tieto>")
            return True

        save_memory(
            osat[1],
            " ".join(osat[2:])
        )

        print(f"🧠 Tallennettu: {osat[1]}")

        return True

    # -------------------------

    if osat[0] == "hae":

        if len(osat) < 2:

            print("Käyttö:")
            print("hae <avain>")
            return True

        tieto = load_memory(osat[1])

        if tieto:

            print(f"🧠 {osat[1]} = {tieto}")

        else:

            print("Tietoa ei löytynyt.")

        return True

    # -------------------------

    if osat[0] == "listaa":

        muistit = list_memories()

        if not muistit:

            print("Muisti on tyhjä.")
            return True

        print("\n=== Muistit ===\n")

        for avain, tieto in muistit:

            print(f"{avain} = {tieto}")

        return True

    # -------------------------
    # MODUULIT
    # -------------------------

    if run_module(command):

        return True

    # -------------------------
    # SMART COMMAND
    # -------------------------

    ehdotus = suggest(
        osat[0],
        COMMANDS + list(MODULES.keys())
    )

    if ehdotus:

        print("")
        print(f"🤔 Tarkoititko '{ehdotus}'?")
        print("")

        return True

    # -------------------------

    print("❌ Tuntematon komento.")

    return True