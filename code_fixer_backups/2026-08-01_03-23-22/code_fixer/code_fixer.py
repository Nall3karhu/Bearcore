import os
import shutil
from datetime import datetime

from modules.improvement_memory.improvement_memory import improvement_memory


BACKUP_FOLDER = "code_fixer_backups"


def create_backup(path):

    if not os.path.exists(path):
        return None

    os.makedirs(
        BACKUP_FOLDER,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    backup_path = os.path.join(
        BACKUP_FOLDER,
        timestamp
    )

    shutil.copytree(
        path,
        backup_path,
        dirs_exist_ok=True
    )

    return backup_path



def code_fixer(args=None):

    print("🐻 Code Fixer käynnissä")

    print("💾 Luodaan varmuuskopio...")

    backup = create_backup(
        "modules"
    )

    if backup:

        print(
            f"✅ Backup luotu: {backup}"
        )

    else:

        print(
            "ℹ️ Backupia ei luotu"
        )


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