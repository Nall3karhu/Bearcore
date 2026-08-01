import json
from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
)


class ReportPage(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "🐻 BearCore Reports"
        )

        self.resize(
            600,
            600
        )


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            QLabel(
                "📊 Pipeline Raportit"
            )
        )


        self.list = QListWidget()

        layout.addWidget(
            self.list
        )


        self.refresh_btn = QPushButton(
            "🔄 Päivitä"
        )

        layout.addWidget(
            self.refresh_btn
        )


        self.refresh_btn.clicked.connect(
            self.load_reports
        )


        self.load_reports()



    def load_reports(self):

        self.list.clear()


        current = Path(__file__).resolve()


        base_dir = None


        for parent in current.parents:

            if parent.name == "BearCore":

                base_dir = parent
                break


        if base_dir is None:

            return


        reports_dir = (
            base_dir /
            "reports"
        )


        if not reports_dir.exists():

            self.list.addItem(
                "❌ Ei raporttikansiota"
            )

            return



        reports = list(
            reports_dir.glob(
                "*.json"
            )
        )


        reports.sort(
            reverse=True
        )


        for report in reports:


            try:

                with open(
                    report,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data = json.load(f)


                module = data.get(
                    "module",
                    "-"
                )

                template = data.get(
                    "template",
                    "-"
                )

                time = data.get(
                    "time",
                    "-"
                )


                self.list.addItem(
                    f"✅ {module} | {template} | {time}"
                )


            except Exception:

                self.list.addItem(
                    f"❌ {report.name}"
                )


        self.list.addItem("")

        self.list.addItem(
            f"Yhteensä: {len(reports)} raporttia"
        )