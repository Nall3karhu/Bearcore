import json
from datetime import datetime
from pathlib import Path


def save_report(module_name, template, steps):

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

    reports_dir.mkdir(
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    report_file = (
        reports_dir /
        f"pipeline_{timestamp}.json"
    )

    data = {
        "module": module_name,
        "template": template,
        "time": timestamp,
        "steps": steps
    }

    try:

        with report_file.open(
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        return report_file

    except KeyboardInterrupt:
        raise

    except Exception as e:

        print(f"❌ Raportin tallennus epäonnistui: {e}")

        return False