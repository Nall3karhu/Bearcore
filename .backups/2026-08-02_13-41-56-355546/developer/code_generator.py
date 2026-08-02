import os
import json


def create_code_module(args=None):

    if not args:

        print("❌ Käyttö: developer create module <nimi>")
        return


    name = args[0].lower()

    module_path = os.path.join(
        "modules",
        name
    )


    if os.path.exists(module_path):

        print("❌ Moduuli on jo olemassa.")
        return


    print("\n🐻 BearCore Code Generator")
    print("=" * 35)

    print(f"Luodaan moduuli: {name}")


    os.makedirs(module_path)


    # Python tiedosto

    with open(
        os.path.join(
            module_path,
            f"{name}.py"
        ),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
f'''def {name}(args=None):

    print("✅ {name}-moduuli toimii!")

    return True
'''
        )


    # init

    open(
        os.path.join(
            module_path,
            "__init__.py"
        ),
        "w",
        encoding="utf-8"
    ).close()



    # config

    with open(
        os.path.join(
            module_path,
            "config.json"
        ),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "name": name,
                "version": "1.0"
            },
            f,
            indent=4
        )



    # README

    with open(
        os.path.join(
            module_path,
            "README.md"
        ),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
f"# {name}\n\nBearCore generated module.\n"
        )



    # testi

    os.makedirs(
        "tests",
        exist_ok=True
    )


    with open(
        os.path.join(
            "tests",
            f"test_{name}.py"
        ),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
f'''from modules.{name}.{name} import {name}


def test_{name}():

    assert {name}() == True
'''
        )



    print("\n✅ Python tiedosto luotu")
    print("✅ Config luotu")
    print("✅ README luotu")
    print("✅ Testi luotu")

    print("\n🟢 Moduuli valmis.")