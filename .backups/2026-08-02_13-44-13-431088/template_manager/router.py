from modules.template_manager.commands.loader import run_command


def route_command(args):

    if not args:

        print("📦 Template Manager")
        print("")
        print("Komennot:")
        print("templates list")
        print("templates info <template>")
        print("templates validate")

        return

    if run_command(args):
        return

    print(f"❌ Tuntematon templates-komento: {' '.join(args)}")