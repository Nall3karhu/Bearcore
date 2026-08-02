import os
import shutil


def auto_fix(args=None):

    print("\n🐻 BearCore Auto Fix")
    print("=" * 35)

    fixed = 0


    # Poistetaan pycachet

    for root, dirs, files in os.walk("."):

        for folder in dirs[:]:

            if folder == "__pycache__":

                path = os.path.join(root, folder)

                try:

                    shutil.rmtree(path)

                    print(f"🧹 Poistettu: {path}")

                    fixed += 1

                except Exception as e:

                    print(f"❌ Virhe: {e}")



    # Tarkistetaan moduulien initit

    modules_path = "modules"


    if os.path.exists(modules_path):

        for module in os.listdir(modules_path):

            path = os.path.join(
                modules_path,
                module
            )


            if os.path.isdir(path):

                init_file = os.path.join(
                    path,
                    "__init__.py"
                )


                if not os.path.exists(init_file):

                    open(
                        init_file,
                        "w"
                    ).close()


                    print(
                        f"📄 Luotu: {init_file}"
                    )

                    fixed += 1



    print("\n======================")

    print(f"🔧 Korjauksia tehty: {fixed}")


    if fixed == 0:

        print("✅ Mitään korjattavaa ei löytynyt.")

    else:

        print("🟢 Korjaukset valmis.")