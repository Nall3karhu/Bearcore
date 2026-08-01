import os
import ast


def check_code(args=None):

    print("\n🐻 BearCore Code Checker")
    print("=" * 35)

    errors = []
    files = 0


    for root, dirs, filenames in os.walk("."):

        for file in filenames:

            if file.endswith(".py"):

                files += 1

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

                    errors.append(
                        {
                            "file": path,
                            "line": e.lineno,
                            "error": e.msg
                        }
                    )


    print(f"\n🐍 Tarkistettu tiedostoja: {files}")


    if errors:

        print("\n❌ Virheitä löytyi:\n")


        for error in errors:

            print(
                f"{error['file']} "
                f"rivi {error['line']}: "
                f"{error['error']}"
            )


    else:

        print("\n✅ Ei syntaksivirheitä.")


    print("\n🟢 Tarkistus valmis.")