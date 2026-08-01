from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)


from core.event_logger import get_events



class DashboardPanel(QWidget):

    def __init__(self):

        super().__init__()


        layout = QVBoxLayout(
            self
        )


        self.title = QLabel(
            "🐻 BearCore Dashboard"
        )


        self.status = QLabel()


        self.modules = QLabel()

        self.reports = QLabel()

        self.backups = QLabel()

        self.events = QLabel()



        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.status
        )

        layout.addWidget(
            self.modules
        )

        layout.addWidget(
            self.reports
        )

        layout.addWidget(
            self.backups
        )

        layout.addWidget(
            self.events
        )


        self.refresh()



    def refresh(self):

        base = (
            Path(__file__)
            .resolve()
            .parent
            .parent
        )


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


        modules = 0
        reports = 0
        backups = 0


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

            event_count = len(
                get_events()
            )

        except:

            event_count = 0



        self.status.setText(
            "🟢 Online"
        )

        self.modules.setText(
            f"📦 Moduuleita: {modules}"
        )

        self.reports.setText(
            f"📊 Raportteja: {reports}"
        )

        self.backups.setText(
            f"💾 Backupeja: {backups}"
        )

        self.events.setText(
            f"📜 Tapahtumia: {event_count}"
        )