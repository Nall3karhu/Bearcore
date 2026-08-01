from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "🐻 BearCore Dashboard"
        )

        self.resize(
            600,
            500
        )


        layout = QVBoxLayout(
            self
        )


        self.title = QLabel(
            "🐻 BearCore Dashboard"
        )

        layout.addWidget(
            self.title
        )


        self.status = QLabel()

        self.modules = QLabel()

        self.templates = QLabel()

        self.reports = QLabel()


        layout.addWidget(
            self.status
        )

        layout.addWidget(
            self.modules
        )

        layout.addWidget(
            self.templates
        )

        layout.addWidget(
            self.reports
        )


        self.refresh_btn = QPushButton(
            "🔄 Päivitä"
        )

        layout.addWidget(
            self.refresh_btn
        )


        self.refresh_btn.clicked.connect(
            self.load_data
        )


        self.load_data()



    def find_bearcore(self):

        current = Path(__file__).resolve()


        for parent in current.parents:

            if parent.name == "BearCore":

                return parent


        return None



    def load_data(self):

        base = self.find_bearcore()


        if not base:

            return


        modules_dir = (
            base /
            "modules"
        )


        templates_dir = (
            base /
            "templates"
        )


        reports_dir = (
            base /
            "reports"
        )


        modules = 0
        templates = 0
        reports = 0



        if modules_dir.exists():

            modules = len(
                [
                    x for x in modules_dir.iterdir()
                    if x.is_dir()
                ]
            )



        if templates_dir.exists():

            templates = len(
                [
                    x for x in templates_dir.iterdir()
                    if x.is_dir()
                ]
            )



        if reports_dir.exists():

            reports = len(
                list(
                    reports_dir.glob("*.json")
                )
            )



        self.status.setText(
            "🟢 Tila: BearCore valmis"
        )


        self.modules.setText(
            f"📦 Moduuleita: {modules}"
        )


        self.templates.setText(
            f"📚 Templateja: {templates}"
        )


        self.reports.setText(
            f"📄 Raportteja: {reports}"
        )