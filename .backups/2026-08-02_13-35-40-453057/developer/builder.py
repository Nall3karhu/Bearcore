from modules.developer.planner import create_plan
from modules.developer.code_generator import create_code_module
from modules.developer.checker import check_code
from modules.developer.tester import run_tests
from modules.developer.history import save_history



def build_module(args=None):

    if not args:

        print("❌ Käyttö: developer build module <nimi>")
        return


    name = args[-1].lower()


    print("\n🐻 BearCore Builder")
    print("=" * 40)


    try:

        print("\n🧠 Suunnitellaan...")
        create_plan([name])


        print("\n🛠️ Luodaan moduuli...")
        create_code_module([name])


        print("\n🔍 Tarkistetaan...")
        check_code()


        print("\n🧪 Testataan...")
        run_tests()


        save_history(
            name,
            "success"
        )


        print("\n🟢 Rakennus onnistui.")


    except Exception as e:

        save_history(
            name,
            "failed"
        )


        print(
            f"\n❌ Rakennus epäonnistui: {e}"
        )