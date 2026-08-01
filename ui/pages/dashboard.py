from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
)

from core.event_logger import get_events



class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "🐻 BearCore Dashboard"
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
                "🐻 BearCore Dashboard"
            )
        )


        self.status = QLabel()

        self.info = QTextEdit()

        self.info.setReadOnly(
            True
        )


        layout.addWidget(
            self.status
        )


        layout.addWidget(
            self.info
        )


        self.refresh_btn = QPushButton(
            "🔄 Päivitä"
        )


        layout.addWidget(
            self.refresh_btn
        )


        self.refresh_btn.clicked.connect(
            self.refresh
        )


        self.refresh()



    def refresh(self):

        base = (
            Path(__file__)
            .resolve()
            .parent
            .parent
            .parent
        )


        modules = 0
        reports = 0
        backups = 0



        modules_dir = (
            base /
            "modules"
        )


        reports_dir = (
            base /
            "reports"
        )


        backups_dir = (
            base /
            "backups"
        )



        if modules_dir.exists():

            modules = len(
                [
                    x for x in modules_dir.iterdir()
                    if x.is_dir()
                    and x.name != "__pycache__"
                ]
            )



        if reports_dir.exists():

            reports = len(
                list(
                    reports_dir.iterdir()
                )
            )



        if backups_dir.exists():

            backups = len(
                list(
                    backups_dir.iterdir()
                )
            )



        try:

            events = get_events()

        except:

            events = []



        text = f"""
🟢 Järjestelmä:
Online


📦 Moduuleita:
{modules}


📊 Raportteja:
{reports}


💾 Backupeja:
{backups}


📜 Tapahtumia:
{len(events)}



--------------------

📜 Viimeisimmät tapahtumat:

"""



        for event in reversed(
            events[-10:]
        ):

            text += (

f"""
🕒 {event.get("time")}

{event.get("event")}

"""

            )



        self.status.setText(
            "🟢 BearCore aktiivinen"
        )


        self.info.setText(
            text
        )