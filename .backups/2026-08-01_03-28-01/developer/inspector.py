import os
import ast


def inspect_module(args=None):

    if not args:

        print("❌ Käyttö: developer inspect <moduuli>")
        return


    name = args[-1]


    path = os.path.join(
        "modules",
        name
    )


    print("\n🐻 BearCore Module Inspector")
    print("=" * 40)


    if not os.path.exists(path):

        print("❌ Moduulia ei löydy.")
        return


    print(f"\nModuuli:")
    print(name)


    print("\n📁 Tiedostot:")

    for file in os.listdir(path):

        print(f"✅ {file}")


    functions = []
    imports = []


    for file in os.listdir(path):

        if file.endswith(".py"):

            filepath = os.path.join(
                path,
                file
            )

            try:

                with open(
                    filepath,
                    "r",
                    encoding="utf-8"
                ) as f:

                    tree = ast.parse(f.read())


                for node in ast.walk(tree):

                    if isinstance(
                        node,
                        ast.FunctionDef
                    ):

                        functions.append(
                            node.name
                        )


                    if isinstance(
                        node,
                        ast.Import
                    ):

                        for item in node.names:

                            imports.append(
                                item.name
                            )


                    if isinstance(
                        node,
                        ast.ImportFrom
                    ):

                        if node.module:

                            imports.append(
                                node.module
                            )


            except Exception:

                pass



    print("\n🧠 Funktiot:")

    if functions:

        for func in functions:

            print(f"✅ {func}")

    else:

        print("Ei funktioita")



    print("\n📦 Importit:")

    if imports:

        for item in sorted(set(imports)):

            print(f"- {item}")

    else:

        print("Ei importteja")



    test_file = os.path.join(
        "tests",
        f"test_{name}.py"
    )


    print("\n🧪 Testi:")

    if os.path.exists(test_file):

        print(f"✅ {test_file}")

    else:

        print("⚠️ Testiä ei löydy")



    print("\n🟢 Tarkistus valmis.")