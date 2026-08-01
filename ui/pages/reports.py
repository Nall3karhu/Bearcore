from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
)


from core.event_logger import get_events



class ReportPage(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "🐻 BearCore Reports"
        )


        self.resize(
            700,
            700
        )


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            QLabel(
                "📊 BearCore System Report"
            )
        )


        self.report = QTextEdit()

        self.report.setReadOnly(
            True
        )


        layout.addWidget(
            self.report
        )


        self.refresh_btn = QPushButton(
            "🔄 Päivitä raportti"
        )


        layout.addWidget(
            self.refresh_btn
        )


        self.refresh_btn.clicked.connect(
            self.generate_report
        )


        self.generate_report()



    def generate_report(self):

        base = (
            Path(__file__)
            .resolve()
            .parent
            .parent
            .parent
        )


        modules = 0
        backups = 0
        reports = 0


        modules_dir = (
            base /
            "modules"
        )


        backup_dir = (
            base /
            "backups"
        )


        reports_dir = (
            base /
            "reports"
        )



        if modules_dir.exists():

            modules = len(
                [
                    x for x in modules_dir.iterdir()
                    if x.is_dir()
                    and x.name != "__pycache__"
                ]
            )


        if backup_dir.exists():

            backups = len(
                list(
                    backup_dir.glob("*")
                )
            )


        if reports_dir.exists():

            reports = len(
                list(
                    reports_dir.glob("*")
                )
            )



        try:

            events = get_events()

        except:

            events = []



        latest = events[-10:]



        text = f"""
🐻 BearCore System Report
========================


📦 Moduulit:
{modules}


📊 Raporttitiedostot:
{reports}


💾 Backupit:
{backups}


📜 Tapahtumia:
{len(events)}


------------------------

📜 Viimeisimmät tapahtumat:

"""


        for event in reversed(latest):

            text += (
                f"""
🕒 {event.get("time")}

{event.get("event")}

"""
            )



        self.report.setText(
            text
        )