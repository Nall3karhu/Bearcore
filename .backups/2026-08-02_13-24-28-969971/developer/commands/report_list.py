import json
from pathlib import Path


def command(args=None):

    if args is None:
        args = []

    if len(args) < 1:
        return False

    if args[0].lower() != "report_list":
        return False

    current = Path(__file__).resolve()

    base_dir = None

    for parent in current.parents:

        if parent.name == "BearCore":

            base_dir = parent
            break

    if base_dir is None:

        print("❌ BearCore-kansiota ei löytynyt.")
        return False

    reports_dir = base_dir / "reports"

    print("📋 Pipeline Reports")
    print("==================")
    print()

    if not reports_dir.exists():

        print("ℹ️ Ei raportteja.")
        return True

    reports = sorted(
        reports_dir.glob("*.json"),
        reverse=True
    )

    if not reports:

        print("ℹ️ Ei raportteja.")
        return True

    for report in reports:

        try:

            with report.open(
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

            print(f"✅ {data.get('module', '-')}")
            print(f"   Template: {data.get('template', '-')}")
            print(f"   Aika: {data.get('time', '-')}")
            print()

        except Exception as e:

            print(f"❌ Virhe luettaessa {report.name}: {e}")

    return True