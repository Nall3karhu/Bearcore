from modules.module_manager.commands.loader import run_command


def route_command(args):

    if not args:

        print("📦 Module Manager")
        print("")
        print("Komennot:")
        print("module list")
        print("module info <nimi>")
        print("module search <hakusana>")
        print("module stats")

        return

    if run_command(args):
        return

    print(f"❌ Tuntematon module-komento: {' '.join(args)}")