import config
from core.logger import logger
from core.database import init_database
from core.command_handler import handle_command
from core.brain import Brain
from core.module_manager import load_modules


def main():

    logger.info("BearCore käynnistetty")

    init_database()

    # Ladataan kaikki moduulit
    load_modules()

    brain = Brain()

    print("=" * 45)
    print(f"{config.APP_NAME} {config.VERSION}")
    print("BearCore käynnissä.")
    print("Kirjoita 'apu' nähdäksesi komennot.")
    print("=" * 45)

    while True:

        command = input("\nBearCore > ").strip()

        if command.lower() in (
            "exit",
            "quit",
            "lopeta"
        ):
            print("👋 Suljetaan BearCore...")
            break

        # Brain käsittelee KAIKKI komennot
        if brain.think(command):
            continue

        # Jos Brain ei osannut, käytetään vanhaa komentojärjestelmää
        if handle_command(command):
            continue

        print("❌ Tuntematon komento.")


if __name__ == "__main__":
    main()