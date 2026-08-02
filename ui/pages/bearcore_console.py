from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QLineEdit,
)


from modules.console.console import execute



class BearCoreConsolePage(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "🐻 BearCore Console"
        )


        self.resize(
            700,
            500
        )


        layout = QVBoxLayout(
            self
        )


        self.title = QLabel(
            "🐻 BearCore Console"
        )


        layout.addWidget(
            self.title
        )


        self.input = QLineEdit()


        self.input.setPlaceholderText(
            "Kirjoita komento..."
        )


        layout.addWidget(
            self.input
        )


        self.run_button = QPushButton(
            "▶ Suorita"
        )


        layout.addWidget(
            self.run_button
        )


        self.output = QTextEdit()


        self.output.setReadOnly(
            True
        )


        layout.addWidget(
            self.output
        )


        self.run_button.clicked.connect(
            self.run_command
        )


        self.input.returnPressed.connect(
            self.run_command
        )



    def run_command(self):

        command = self.input.text()


        if not command:

            return


        try:

            result = execute(
                command
            )


            self.output.append(
                str(result)
            )


        except Exception as e:

            self.output.append(
                f"❌ Virhe: {e}"
            )


        self.input.clear()