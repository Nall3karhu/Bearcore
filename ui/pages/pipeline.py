import subprocess
import sys

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
)


class PipelinePage(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "🐻 BearCore Pipeline"
        )

        self.resize(
            600,
            500
        )


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            QLabel(
                "🚀 Developer Pipeline"
            )
        )


        self.module_input = QLineEdit()

        self.module_input.setPlaceholderText(
            "Moduulin nimi"
        )

        layout.addWidget(
            self.module_input
        )


        self.template_input = QLineEdit()

        self.template_input.setPlaceholderText(
            "Template (esim. api)"
        )

        layout.addWidget(
            self.template_input
        )


        self.run_btn = QPushButton(
            "🚀 Käynnistä Pipeline"
        )

        layout.addWidget(
            self.run_btn
        )


        self.output = QTextEdit()

        self.output.setReadOnly(
            True
        )

        layout.addWidget(
            self.output
        )


        self.run_btn.clicked.connect(
            self.run_pipeline
        )


    def run_pipeline(self):

        module = (
            self.module_input.text()
            .strip()
            .lower()
        )


        template = (
            self.template_input.text()
            .strip()
            .lower()
        )


        if not module:

            self.output.append(
                "❌ Anna moduulin nimi"
            )

            return


        if not template:

            template = "empty"


        self.output.append(
            f"🐻 Pipeline: {module}"
        )

        self.output.append(
            f"📦 Template: {template}"
        )

        self.output.append(
            ""
        )


        try:

            result = subprocess.run(

                [
                    sys.executable,
                    "main.py",
                    "developer",
                    "pipeline",
                    module,
                    template
                ],

                capture_output=True,

                text=True

            )


            self.output.append(
                result.stdout
            )


            if result.stderr:

                self.output.append(
                    result.stderr
                )


        except Exception as e:

            self.output.append(
                f"❌ Virhe: {e}"
            )