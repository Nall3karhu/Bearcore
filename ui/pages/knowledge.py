from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit
)


class KnowledgePage(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "📚 Knowledge"
        )


        self.resize(
            700,
            500
        )


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            QLabel(
                "📚 BearCore Knowledge"
            )
        )


        self.output = QTextEdit()

        self.output.setReadOnly(
            True
        )


        self.output.setText(
            "Tietokanta valmis.\n\n"
            "Tähän tulee tietohaut ja muisti."
        )


        layout.addWidget(
            self.output
        )