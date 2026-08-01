from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
)


class TemplatePage(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "🐻 BearCore Template Browser"
        )

        self.resize(
            500,
            600
        )


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            QLabel(
                "📦 BearCore Templates"
            )
        )


        self.list = QListWidget()

        layout.addWidget(
            self.list
        )


        self.refresh = QPushButton(
            "🔄 Päivitä"
        )

        layout.addWidget(
            self.refresh
        )


        self.refresh.clicked.connect(
            self.load_templates
        )


        self.load_templates()



    def load_templates(self):

        self.list.clear()


        current = Path(__file__).resolve()


        base_dir = None


        for parent in current.parents:

            if parent.name == "BearCore":

                base_dir = parent
                break


        if base_dir is None:

            self.list.addItem(
                "❌ BearCore ei löytynyt"
            )

            return


        templates_dir = (
            base_dir /
            "templates"
        )


        if not templates_dir.exists():

            self.list.addItem(
                "❌ Templates puuttuu"
            )

            return


        templates = []


        for item in templates_dir.iterdir():

            if item.is_dir():

                templates.append(
                    item.name
                )


        templates.sort()


        for template in templates:

            self.list.addItem(
                f"✅ {template}"
            )


        self.list.addItem("")
        self.list.addItem(
            f"Yhteensä: {len(templates)}"
        )