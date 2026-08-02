from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit
)


class PipelinePage(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "🚀 Pipeline"
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
                "🚀 BearCore Pipeline"
            )
        )


        self.output = QTextEdit()

        self.output.setReadOnly(
            True
        )


        self.output.setText(
            "Pipeline valmis.\n\n"
            "Task → Worker → Result"
        )


        layout.addWidget(
            self.output
        )