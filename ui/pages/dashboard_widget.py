from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)


class DashboardWidget(QWidget):

    def __init__(self):

        super().__init__()


        layout = QVBoxLayout(
            self
        )


        self.title = QLabel(
            "🐻 BearCore Status"
        )

        self.status = QLabel()

        self.modules = QLabel()

        self.templates = QLabel()

        self.backup = QLabel()


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
            self.templates
        )

        layout.addWidget(
            self.backup
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

        templates_dir = (
            base /
            "templates"
        )


        modules = 0
        templates = 0


        if modules_dir.exists():

            modules = len(
                [
                    x for x in modules_dir.iterdir()
                    if x.is_dir()
                    and x.name != "__pycache__"
                ]
            )


        if templates_dir.exists():

            templates = len(
                [
                    x for x in templates_dir.iterdir()
                    if x.is_dir()
                ]
            )


        self.status.setText(
            "🟢 Online"
        )

        self.modules.setText(
            f"📦 Moduuleita: {modules}"
        )

        self.templates.setText(
            f"📚 Templateja: {templates}"
        )

        self.backup.setText(
            "💾 Backup: OK"
        )