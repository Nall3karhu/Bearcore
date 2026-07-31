import os

from modules.developer.create_module import create_module
from modules.developer.create_ui import create_ui
from modules.developer.scan import scan_project
from modules.developer.analyze import analyze_project
from modules.developer.tester import run_tests
from modules.developer.checker import check_code
from modules.developer.suggest import suggest_fixes



def verify_module(name):

    path = os.path.join("modules", name)

    if not os.path.exists(path):

        print("❌ Moduulia ei löydy.")
        return


    print(f"\n🔍 Tarkistetaan {name}")

    for file in os.listdir(path):

        print(f"📄 {file}")



def verify_all():

    print("\n🔍 Moduulit:\n")

    for folder in os.listdir("modules"):

        path = os.path.join("modules", folder)

        if os.path.isdir(path):

            print(f"✅ {folder}")



def developer(args):


    if len(args) == 0:

        print("""
🐻 BearCore Developer

Komennot:

developer status

developer scan

developer analyze

developer check

developer suggest

developer test all

developer new module <nimi>

developer new ui <nimi>

developer verify module <nimi>

developer verify all

""")
        return



    if args[0] == "status":

        print("🛠️ Developer toimii.")
        return



    if args[0] == "scan":

        scan_project()
        return



    if args[0] == "analyze":

        analyze_project()
        return



    if args[0] == "check":

        check_code()
        return



    if args[0] == "suggest":

        suggest_fixes()
        return



    if args[0] == "test":

        run_tests()
        return



    if len(args) >= 3:

        if args[0] == "new" and args[1] == "module":

            create_module(args[2:])
            return


        if args[0] == "new" and args[1] == "ui":

            create_ui(args[2:])
            return



    if len(args) >= 3:

        if args[0] == "verify" and args[1] == "module":

            verify_module(args[2])
            return



    if len(args) >= 2:

        if args[0] == "verify" and args[1] == "all":

            verify_all()
            return



    print("❌ Tuntematon developer-komento.")