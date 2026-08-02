import json
from pathlib import Path


def command(args):

    if len(args) < 1:
        return False


    if args[0] != "report_list":
        return False


    current = Path(__file__).resolve()

    base_dir = None


    for parent in current.parents:

        if parent.name == "BearCore":

            base_dir = parent
            break


    if base_dir is None:

        print("❌ BearCore-kansiota ei löytynyt.")
        return True


    reports_dir = base_dir / "reports"


    print("🐻 Pipeline Reports")
    print("==================")
    print("")


    if not reports_dir.exists():

        print("❌ Raporttikansiota ei löytynyt.")

        return True


    reports = list(
        reports_dir.glob(
            "*.json"
        )
    )


    reports.sort(
        reverse=True
    )


    if not reports:

        print(
            "ℹ️ Ei raportteja."
        )

        return True



    for report in reports:


        try:

            with open(
                report,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)


            print(
                f"✅ {data.get('module','-')}"
            )

            print(
                f"   Template: {data.get('template','-')}"
            )

            print(
                f"   Aika: {data.get('time','-')}"
            )

            print("")


        except Exception:

            print(
                f"❌ Virhe raportissa: {report.name}"
            )


    print(
        f"Yhteensä: {len(reports)} raporttia"
    )


    return True