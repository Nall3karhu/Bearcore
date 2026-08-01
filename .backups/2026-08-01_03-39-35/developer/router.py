from modules.developer.commands.loader import run_command



def route_command(args):

    if not args:

        print("🐻 Developer Router aktiivinen")

        return


    if run_command(args):

        return


    print("❌ Tuntematon developer-komento.")