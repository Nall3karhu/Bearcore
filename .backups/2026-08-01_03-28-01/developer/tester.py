import os
import subprocess
import sys


def run_tests(args=None):

    print("\n🐻 BearCore Test System")
    print("=" * 35)

    test_path = "tests"

    if not os.path.exists(test_path):

        print("❌ tests-kansiota ei löytynyt.")
        return


    tests = []

    for file in os.listdir(test_path):

        if file.startswith("test_") and file.endswith(".py"):

            tests.append(file)


    if not tests:

        print("⚠️ Testejä ei löytynyt.")
        return


    print(f"\n🧪 Testejä löytyi: {len(tests)}\n")


    success = 0
    failed = 0


    for test in tests:

        path = os.path.join(test_path, test)

        print(f"▶️ Ajetaan: {test}")


        result = subprocess.run(
            [
                sys.executable,
                path
            ],
            capture_output=True,
            text=True
        )


        if result.returncode == 0:

            print(f"✅ {test}")

            success += 1


        else:

            print(f"❌ {test}")

            print(result.stderr)

            failed += 1



    print("\n=========================")

    print(f"✅ Onnistui: {success}")
    print(f"❌ Epäonnistui: {failed}")

    print("=========================")

    if failed == 0:

        print("🟢 Kaikki testit läpäisty.")

    else:

        print("🔴 Virheitä löytyi.")