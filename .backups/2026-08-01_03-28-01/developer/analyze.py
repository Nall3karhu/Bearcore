import os
import ast


def analyze_project(args=None):

    print("\n🐻 BearCore Code Analysis")
    print("=" * 35)

    python_files = 0
    functions = 0
    imports = set()
    modules = []


    for root, dirs, files in os.walk("."):

        for file in files:

            if file.endswith(".py"):

                python_files += 1

                path = os.path.join(root, file)


                if "modules" in root:

                    parts = root.split(os.sep)

                    if "modules" in parts:

                        index = parts.index("modules")

                        if len(parts) > index + 1:

                            name = parts[index + 1]

                            if name not in modules:
                                modules.append(name)


                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        tree = ast.parse(f.read())


                    for node in ast.walk(tree):

                        if isinstance(node, ast.FunctionDef):

                            functions += 1


                        if isinstance(node, ast.Import):

                            for item in node.names:

                                imports.add(item.name)


                        if isinstance(node, ast.ImportFrom):

                            if node.module:

                                imports.add(node.module)


                except Exception:

                    pass



    print(f"\n🐍 Python tiedostoja: {python_files}")
    print(f"🔧 Funktioita löydetty: {functions}")


    print("\n🔌 Moduulit:")

    for module in sorted(modules):

        print(f"✅ {module}")


    print("\n📦 Importit:")

    for item in sorted(imports):

        print(f"- {item}")


    print("\n🟢 Analyysi valmis.")