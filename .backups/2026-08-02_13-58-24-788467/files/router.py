from modules.files.commands.loader import run_command


def route(args):

    if not args:

        print("📁 File Manager")
        print("")
        print("Komennot:")
        print("files mkdir <kansio>")
        print("files touch <tiedosto>")
        print("files ls")
        print("files tree")
        print("files pwd")
        print("files cat <tiedosto>")
        print("files rm <kohde>")
        print("files mv <vanha> <uusi>")
        print("files cp <lähde> <kohde>")
        print("files open <tiedosto>")
        return

    if run_command(args):
        return

    print(f"❌ Tuntematon files-komento: {' '.join(args)}")