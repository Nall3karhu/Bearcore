import subprocess
from datetime import datetime
from modules.improvement_memory.improvement_memory import improvement_memory
from modules.auto_repair.auto_repair import auto_repair


MAX_ATTEMPTS = 3


def repair_pipeline(args=None):

    print("🐻 Repair Pipeline käynnissä")

    if not args:
        print("ℹ️ Ei korjauspyyntöä")
        return True

    error = args[0] if isinstance(args, list) else args


    print("🔎 Tarkistetaan aiempi muisti...")


    improvement_memory(
        [
            "search",
            error[:50]
        ]
    )


    for attempt in range(
        1,
        MAX_ATTEMPTS + 1
    ):

        print(
            f"🔧 Korjauskierros {attempt}/{MAX_ATTEMPTS}"
        )


        print(
            "🤖 Kutsutaan Auto Repairia..."
        )


        auto_repair(
            [
                error
            ]
        )


        print(
            "🧪 Testataan korjauksen jälkeen..."
        )


        result = subprocess.run(
            [
                "python",
                "-m",
                "pytest"
            ],
            capture_output=True,
            text=True
        )


        if result.returncode == 0:

            print(
                "✅ Testit läpi"
            )

            improvement_memory(
                [
                    "save",
                    error[:200],
                    "Auto Repair onnistui"
                ]
            )

            return True


        print(
            "❌ Testit epäonnistuivat"
        )


        if attempt < MAX_ATTEMPTS:
            print(
                "🔁 Uusi yritys..."
            )


    print(
        "🛑 Korjaus epäonnistui"
    )


    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    filename = (
        f"repair_failed_{timestamp}.log"
    )


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            result.stdout +
            "\n" +
            result.stderr
        )


    improvement_memory(
        [
            "save",
            error[:200],
            "Auto Repair epäonnistui"
        ]
    )


    return False