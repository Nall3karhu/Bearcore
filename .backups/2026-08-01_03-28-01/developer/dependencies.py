import os
import ast


def analyze_dependencies(args=None):

    print("\n🐻 BearCore Dependency Analyzer")
    print("=" * 40)


    modules_path = "modules"


    if not os.path.exists(modules_path):

        print("❌ modules-kansiota ei löytynyt.")
        return



    for module in sorted(os.listdir(modules_path)):

        module_path = os.path.join(
            modules_path,
            module
        )


        if not os.path.isdir(module_path):

            continue


        print(f"\n📦 {module}")


        found = False


        for file in os.listdir(module_path):

            if file.endswith(".py"):

                path = os.path.join(
                    module_path,
                    file
                )


                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        tree = ast.parse(
                            f.read()
                        )


                    for node in ast.walk(tree):

                        if isinstance(
                            node,
                            ast.Import
                        ):

                            for item in node.names:

                                print(
                                    f" └── {item.name}"
                                )

                                found = True


                        if isinstance(
                            node,
                            ast.ImportFrom
                        ):

                            if node.module:

                                print(
                                    f" └── {node.module}"
                                )

                                found = True


                except Exception:

                    pass



        if not found:

            print(" └── Ei riippuvuuksia")



    print("\n🟢 Riippuvuusanalyysi valmis.")