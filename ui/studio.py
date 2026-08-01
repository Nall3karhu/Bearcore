import sys
import subprocess

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QListWidget,
    QLabel,
)
from PySide6.QtCore import QTimer


class BearCoreStudio(QMainWindow):

    def __init__(self):
        super().__init__()

        self.process = None

        self.setWindowTitle("🐻 BearCore Studio")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        # Moduulit
        left = QVBoxLayout()

        left.addWidget(QLabel("Moduulit"))

        self.modules = QListWidget()

        left.addWidget(self.modules)

        # Konsoli
        right = QVBoxLayout()

        right.addWidget(QLabel("BearCore"))

        self.console = QTextEdit()

        self.console.setReadOnly(True)

        right.addWidget(self.console)

        # Napit
        buttons = QHBoxLayout()

        self.start_btn = QPushButton("▶ Käynnistä")

        self.stop_btn = QPushButton("■ Pysäytä")

        buttons.addWidget(self.start_btn)
        buttons.addWidget(self.stop_btn)

        right.addLayout(buttons)

        layout.addLayout(left, 1)
        layout.addLayout(right, 3)

        self.start_btn.clicked.connect(self.start_bearcore)
        self.stop_btn.clicked.connect(self.stop_bearcore)

        self.timer = QTimer()
        self.timer.timeout.connect(self.read_output)

    def start_bearcore(self):

        if self.process:
            return

        self.console.append("Käynnistetään BearCore...\n")

        self.process = subprocess.Popen(
            ["python", "main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            text=True,
            bufsize=1,
        )

        self.timer.start(100)

    def read_output(self):

        if not self.process:
            return

        while True:

            line = self.process.stdout.readline()

            if not line:
                break

            self.console.append(line.rstrip())

    def stop_bearcore(self):

        if not self.process:
            return

        try:
            self.process.stdin.write("lopeta\n")
            self.process.stdin.flush()
        except Exception:
            pass

        self.process = None

        self.console.append("\nBearCore pysäytetty")


app = QApplication(sys.argv)

window = BearCoreStudio()

window.show()

sys.exit(app.exec())