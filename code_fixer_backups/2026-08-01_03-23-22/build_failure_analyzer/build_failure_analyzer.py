import os
from modules.auto_repair.auto_repair import auto_repair
from modules.improvement_memory.improvement_memory import improvement_memory


def build_failure_analyzer(args=None):

    print("🐻 Build Failure Analyzer käynnissä")

    log_file = "safe_builder_error.log"

    if not os.path.exists(log_file):
        print("ℹ️ Ei virheraporttia löydetty")
        return True

    try:
        with open(
            log_file,
            "r",
            encoding="utf-8"
        ) as f:
            error = f.read()

        if not error.strip():
            print("✅ Virheraportti tyhjä")
            return True

        print("📄 Virheraportti löydetty")
        print("======================")

        print("🔎 Tarkistetaan aiempi historia...")

        memory_result = improvement_memory(
            [
                "search",
                error[:50]
            ]
        )

        if memory_result:
            print("💡 Löytyi vastaava aiempi tapaus")
        else:
            print("ℹ️ Ei aiempaa ratkaisua")

        if "ModuleNotFoundError" in error:
            print("🔴 Löytyi: ModuleNotFoundError")
            print("💡 Tarkista importit ja moduulipolut")

        elif "ImportError" in error:
            print("🔴 Löytyi: ImportError")
            print("💡 Tarkista moduulin nimi")

        elif "SyntaxError" in error:
            print("🔴 Löytyi: SyntaxError")
            print("💡 Tarkista Python-koodi")

        elif "AssertionError" in error:
            print("🔴 Löytyi: AssertionError")
            print("💡 Testin odotus ei täyty")

        else:
            print("🔴 Tuntematon virhe")
            print(error[:500])

        print("🐻 Lähetetään Auto Repairille...")

        auto_repair(
            [error]
        )

        return False

    except Exception as e:

        print("❌ Analyzer virhe:")
        print(e)

        return False