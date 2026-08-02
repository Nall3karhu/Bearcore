from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit
)


class ReportPage(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "📊 Reports"
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
                "📊 BearCore Reports"
            )
        )


        self.output = QTextEdit()

        self.output.setReadOnly(
            True
        )


        self.output.setText(
            "Raporttijärjestelmä valmis."
        )


        layout.addWidget(
            self.output
        )