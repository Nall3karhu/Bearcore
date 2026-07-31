from core.memory import save_memory, load_memory, list_memories
from modules.weather.weather import weather


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
sää
lopeta
""")

    elif osat[0] == "muista":

        if len(osat) < 3:
            print("Käyttö: muista <avain> <tieto>")
            return True

        avain = osat[1]
        tieto = " ".join(osat[2:])

        save_memory(avain, tieto)

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

    elif osat[0] == "sää":
        weather()

    elif osat[0] == "lopeta":
        print("BearCore suljetaan...")
        return False

    else:
        print("Tuntematon komento. Kirjoita 'apu'.")

    return True