from modules.developer.commands.loader import run_command


def route_command(args=None):

    if args is None:
        args = []

    if not args:

        print("🧰 Developer Router aktiivinen")
        print()
        print("Käyttö:")
        print("developer analyze")
        print("developer build")
        print("developer test")
        print("developer fix")
        print("developer status")

        return True

    try:

        if run_command(args):
            return True

        print(f"❌ Tuntematon developer-komento: {' '.join(args)}")
        return False

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Developer Router -virhe: {e}")
        return False