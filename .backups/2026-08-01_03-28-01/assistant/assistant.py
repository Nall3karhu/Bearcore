from core.module_manager import run_module


def assistant(args=None):

    print("""
=========================
🐻 BearCore Assistant
Kirjoita 'poistu' poistuaksesi.
=========================
""")

    while True:

        command = input("Sinä > ").strip()

        if command.lower() in ["poistu", "exit", "lopeta"]:
            print("Assistant suljetaan.")
            break

        lower = command.lower()

        # Projekti
        if "projekti" in lower or "tila" in lower:
            run_module("project")
            continue

        # Selain
        if lower.startswith("etsi netistä"):
            haku = command[13:].strip()
            run_module(f"browser {haku}")
            continue

        # Tiedostot
        if lower.startswith("avaa "):
            tiedosto = command[5:].strip()
            run_module(f"files read {tiedosto}")
            continue

        if lower.startswith("etsi tiedosto"):
            haku = command[13:].strip()
            run_module(f"files find {haku}")
            continue

        # Muisti
        if lower.startswith("muista "):
            run_module("ai")
            print("Vihje: Käytä AI:n muistitoimintoa.")
            continue

        print("🤖 En vielä ymmärtänyt tuota.")