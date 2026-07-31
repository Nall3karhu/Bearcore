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

        command = input("\nBearCore > ")

        if command == "brain":
            brain.think(input("Ajatus > "))
            continue

        if not handle_command(command):
            break


if __name__ == "__main__":
    main()