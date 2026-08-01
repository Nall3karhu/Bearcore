from modules.module_validator.module_validator import module_validator
from modules.build_failure_analyzer.build_failure_analyzer import build_failure_analyzer
from modules.repair_pipeline.repair_pipeline import repair_pipeline
import subprocess


def safe_builder(args=None):

    print("🐻 Safe Builder käynnissä")

    if not args:
        print("❌ Moduulia ei annettu")
        return False

    print("🔍 Tarkistetaan moduulin rakenne...")

    if not module_validator(args):
        print("❌ Validointi epäonnistui")
        return False

    print("✅ Validointi onnistui")

    print("🧪 Ajetaan testit...")

    result = subprocess.run(
        ["python", "-m", "pytest"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("✅ Testit läpi")
        return True

    print("❌ Testit epäonnistuivat")

    with open(
        "safe_builder_error.log",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(
            result.stdout +
            "\n" +
            result.stderr
        )

    print("📄 Virheraportti tallennettu")

    print("🐻 Käynnistetään analyysi...")

    build_failure_analyzer()

    print("🔧 Käynnistetään repair pipeline...")

    return repair_pipeline(
        [result.stdout + result.stderr]
    )