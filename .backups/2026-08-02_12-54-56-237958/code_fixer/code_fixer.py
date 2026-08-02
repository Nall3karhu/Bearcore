from pathlib import Path

from modules.backup_manager.backup_manager import backup_manager
from modules.improvement_memory.improvement_memory import improvement_memory


def code_fixer(args=None):

    print("🐻 Code Fixer käynnissä")

    print("💾 Luodaan varmuuskopio...")

    if not backup_manager():
        print("⚠️ Varmuuskopion luonti epäonnistui.")
        return False

    print("🔍 Tarkistetaan moduulirakennetta...")

    project_root = Path(__file__).resolve().parents[2]
    modules_path = project_root / "modules"

    fixed = []

    for root, dirs, files in modules_path.walk():

        python_files = [f for f in files if f.endswith(".py")]

        if python_files:

            init_file = root / "__init__.py"

            if not init_file.exists():

                init_file.touch()

                fixed.append(str(init_file))

                print(f"✅ Luotu: {init_file}")

    if fixed:
        solution = f"Luotiin {len(fixed)} __init__.py tiedostoa"
    else:
        solution = "Ei korjattavaa löytynyt"
        print("✅ Rakenne kunnossa")

    improvement_memory(
        [
            "save",
            "code_fixer",
            solution
        ]
    )

    print("🐻 Code Fixer valmis")

    return True