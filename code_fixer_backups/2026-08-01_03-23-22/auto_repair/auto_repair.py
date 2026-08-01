from modules.improvement_memory.improvement_memory import improvement_memory
from modules.code_fixer.code_fixer import code_fixer


def auto_repair(args=None):

    print("🐻 Auto Repair käynnissä")

    if not args:
        print("ℹ️ Ei korjattavaa")
        return True

    error = args[0] if isinstance(args, list) else args

    print("🔎 Tarkistetaan aiemmat ratkaisut...")

    improvement_memory(
        [
            "search",
            error[:50]
        ]
    )

    solution = "Ei automaattista korjausta"


    print("🔍 Analysoidaan virhettä...")


    if "No module named" in error:

        print(
            "🔧 Moduulivirhe havaittu"
        )

        print(
            "🐻 Käynnistetään Code Fixer..."
        )

        code_fixer()

        solution = (
            "Code Fixer suoritettiin "
            "moduulirakenteelle"
        )


    elif "ModuleNotFoundError" in error:

        print(
            "🔧 ModuleNotFoundError havaittu"
        )

        code_fixer()

        solution = (
            "Tarkistettiin moduulirakenne"
        )


    elif "SyntaxError" in error:

        solution = (
            "SyntaxError vaatii kooditarkistuksen"
        )


    else:

        solution = (
            "Tuntematon virhe"
        )


    improvement_memory(
        [
            "save",
            error[:200],
            solution
        ]
    )

    print(
        "✅ Auto Repair valmis"
    )

    return True