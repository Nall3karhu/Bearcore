from core.memory import save_memory, load_memory, list_memories
from core.module_manager import run_module


def handle_command(command):

    osat = command.strip().split()

    if len(osat) == 0:
        return True

    if osat[0] == "apu":

        print("""
Komennot:

muista <avain> <tieto>
hae <avain>
listaa

Moduulit:
sää
github
developer

lopeta
""")

    elif osat[0] == "muista":

        if len(osat) < 3:
            print("Käyttö: muista <avain> <tieto>")
            return True

        save_memory(osat[1], " ".join(osat[2:]))

    elif osat[0] == "hae":

        if len(osat) < 2:
            print("Käyttö: hae <avain>")
            return True

        tulos = load_memory(osat[1])

        if tulos:
            print(f"Löytyi: {tulos}")
        else:
            print("Tietoa ei löytynyt.")

    elif osat[0] == "listaa":

        muistit = list_memories()

        if muistit:

            print("\n=== Muistit ===")

            for avain, tieto in muistit:
                print(f"{avain} = {tieto}")

        else:
            print("Muisti on tyhjä.")

    elif osat[0] == "lopeta":

        print("BearCore suljetaan...")
        return False

    # 👇 TÄRKEÄ MUUTOS
    elif run_module(command):
        pass

    else:

        print("Tuntematon komento.")

    return True