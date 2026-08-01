import subprocess
import sys

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
)


class CreateModulePage(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "🐻 BearCore - Luo moduuli"
        )

        self.resize(
            500,
            450
        )


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            QLabel("🐻 Luo uusi moduuli")
        )


        self.name_input = QLineEdit()

        self.name_input.setPlaceholderText(
            "Moduulin nimi"
        )

        layout.addWidget(
            self.name_input
        )


        self.template_input = QLineEdit()

        self.template_input.setPlaceholderText(
            "Template (esim. api)"
        )

        layout.addWidget(
            self.template_input
        )


        self.create_btn = QPushButton(
            "🚀 Luo moduuli"
        )

        layout.addWidget(
            self.create_btn
        )


        self.output = QTextEdit()

        self.output.setReadOnly(
            True
        )

        layout.addWidget(
            self.output
        )


        self.create_btn.clicked.connect(
            self.create_module
        )


    def create_module(self):

        name = (
            self.name_input.text()
            .strip()
            .lower()
        )


        template = (
            self.template_input.text()
            .strip()
            .lower()
        )


        if not name:

            self.output.append(
                "❌ Anna moduulin nimi"
            )

            return


        if not template:

            template = "empty"



        self.output.append(
            f"🐻 Luodaan: {name}"
        )

        self.output.append(
            f"📦 Template: {template}"
        )

        self.output.append(
            ""
        )


        try:

            process = subprocess.run(

                [
                    sys.executable,
                    "main.py",
                    "developer",
                    "pipeline",
                    name,
                    template
                ],

                capture_output=True,

                text=True

            )


            self.output.append(
                process.stdout
            )


            if process.stderr:

                self.output.append(
                    process.stderr
                )


        except Exception as e:

            self.output.append(
                f"❌ Virhe: {e}"
            )