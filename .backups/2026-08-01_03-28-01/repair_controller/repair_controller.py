from modules.code_fixer.code_fixer import code_fixer
from modules.repair_pipeline.repair_pipeline import repair_pipeline
from modules.improvement_memory.improvement_memory import improvement_memory


def repair_controller(args=None):

    print("🐻 Repair Controller käynnissä")

    if not args:
        print("ℹ️ Ei korjauspyyntöä")
        return True

    error = args[0] if isinstance(args, list) else args

    print("🔎 Tallennetaan korjaustapahtuma")

    improvement_memory(
        [
            "save",
            error[:200],
            "Repair Controller aloitti korjausprosessin"
        ]
    )

    print("🔧 Käynnistetään Code Fixer")

    code_fixer()


    print("🧪 Käynnistetään Repair Pipeline")

    result = repair_pipeline(
        [
            error
        ]
    )


    if result:

        print(
            "✅ Repair Controller onnistui"
        )

    else:

        print(
            "❌ Repair Controller epäonnistui"
        )


    return result