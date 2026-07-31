import config
from core.logger import logger
from core.database import init_database
from core.command_handler import handle_command


def main():
    logger.info("BearCore käynnistetty")
    init_database()

    print("=" * 40)
    print(f"{config.APP_NAME} v{config.VERSION}")
    print("Kirjoita 'apu' nähdäksesi komennot.")
    print("=" * 40)

    while True:
        komento = input("\nBearCore > ")

        if not handle_command(komento):
            break


if __name__ == "__main__":
    main()