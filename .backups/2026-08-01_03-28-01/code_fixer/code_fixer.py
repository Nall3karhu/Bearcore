import os

from modules.backup_manager.backup_manager import backup_manager
from modules.improvement_memory.improvement_memory import improvement_memory


def code_fixer(args=None):

    print("🐻 Code Fixer käynnissä")


    print("💾 Luodaan varmuuskopio...")


    backup = backup_manager()


    if backup:

        print(
            "✅ Backup valmis:"
        )

        print(
            backup
        )

    else:

        print(
            "❌ Backup epäonnistui"
        )

        return False



    fixed = []


    print(
        "🔍 Tarkistetaan moduulirakennetta..."
    )


    for root, dirs, files in os.walk(
        "modules"
    ):


        python_files = [
            f for f in files
            if f.endswith(".py")
        ]


        if python_files:


            init_file = os.path.join(
                root,
                "__init__.py"
            )


            if not os.path.exists(
                init_file
            ):

                open(
                    init_file,
                    "w",
                    encoding="utf-8"
                ).close()


                fixed.append(
                    init_file
                )


                print(
                    f"✅ Luotu: {init_file}"
                )



    if fixed:

        solution = (
            f"Luotiin {len(fixed)} "
            "__init__.py tiedostoa"
        )

    else:

        solution = (
            "Ei korjattavaa löytynyt"
        )

        print(
            "✅ Rakenne kunnossa"
        )



    improvement_memory(
        [
            "save",
            "code_fixer",
            solution
        ]
    )


    print(
        "🐻 Code Fixer valmis"
    )


    return True