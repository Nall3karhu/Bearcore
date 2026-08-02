import os
import ast


def suggest_fixes(args=None):

    print("\n🐻 BearCore Fix Suggestions")
    print("=" * 35)

    found = False


    for root, dirs, files in os.walk("."):

        # Ohitetaan välimuistit
        if "__pycache__" in root:
            continue


        for file in files:

            if not file.endswith(".py"):
                continue

            # Älä tarkista itseään
            if file == "suggest.py":
                continue


            path = os.path.join(root, file)


            try:

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    code = f.read()


                ast.parse(code)


            except SyntaxError as e:

                found = True

                print("\n❌ Ongelma löytyi:")
                print(f"📄 {path}")
                print(f"📍 Rivi {e.lineno}")

                print("\nVirhe:")
                print(e.msg)

                print("\nEhdotus:")
                print(
                    "Tarkista rivin Python-syntaksi."
                )


    if not found:

        print("\n✅ Ei korjausehdotuksia.")


    print("\n🟢 Tarkistus valmis.")