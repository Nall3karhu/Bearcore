from modules.developer.commands.loader import run_command


def route_command(args):

    if not args:

        print("🧠 Developer Router aktiivinen")
        print("")
        print("Käyttö:")
        print("developer analyze")
        print("developer build")
        print("developer test")
        print("developer fix")
        print("developer status")

        return

    if run_command(args):
        return

    print(f"❌ Tuntematon developer-komento: {' '.join(args)}")