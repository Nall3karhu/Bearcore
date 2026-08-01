import sys
import os
import json

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(BASE_DIR)
)


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
    QGroupBox,
    QLineEdit,
)



class BearCoreStudio(QMainWindow):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "🐻 BearCore Studio"
        )


        self.resize(
            1400,
            800
        )


        self.all_modules = {}

        self.current_module = None



        central = QWidget()

        self.setCentralWidget(
            central
        )


        main = QVBoxLayout(
            central
        )


        # Yläpalkki

        self.status = QLabel()

        main.addWidget(
            self.status
        )



        content = QHBoxLayout()



        # Moduulit

        left = QVBoxLayout()


        left.addWidget(
            QLabel(
                "📦 Moduulit"
            )
        )


        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "🔍 Hae moduulia..."
        )


        left.addWidget(
            self.search
        )


        self.modules = QListWidget()


        self.modules.itemClicked.connect(
            self.select_module
        )


        left.addWidget(
            self.modules
        )



        # Inspector

        middle = QVBoxLayout()


        middle.addWidget(
            QLabel(
                "🐻 Module Inspector"
            )
        )


        self.info = QTextEdit()

        self.info.setReadOnly(
            True
        )


        middle.addWidget(
            self.info
        )



        self.open_btn = QPushButton(
            "📂 Avaa kansio"
        )


        self.reload_btn = QPushButton(
            "🔄 Reload"
        )


        middle.addWidget(
            self.open_btn
        )

        middle.addWidget(
            self.reload_btn
        )



        self.open_btn.clicked.connect(
            self.open_folder
        )



        # Console

        right = QVBoxLayout()


        right.addWidget(
            QLabel(
                "🐻 Console"
            )
        )


        self.console = QTextEdit()

        self.console.setReadOnly(
            True
        )


        right.addWidget(
            self.console
        )



        # Tools

        tools = QGroupBox(
            "🐻 BearCore Tools"
        )


        tool_layout = QVBoxLayout()



        self.dashboard_btn = QPushButton(
            "🐻 Dashboard"
        )


        self.create_btn = QPushButton(
            "➕ Luo moduuli"
        )


        self.template_btn = QPushButton(
            "📦 Templates"
        )


        self.pipeline_btn = QPushButton(
            "🚀 Pipeline"
        )


        self.report_btn = QPushButton(
            "📊 Raportit"
        )


        self.refresh_btn = QPushButton(
            "🔄 Päivitä"
        )



        for button in [

            self.dashboard_btn,
            self.create_btn,
            self.template_btn,
            self.pipeline_btn,
            self.report_btn,
            self.refresh_btn

        ]:

            tool_layout.addWidget(
                button
            )



        tools.setLayout(
            tool_layout
        )


        right.addWidget(
            tools
        )



        content.addLayout(
            left,
            1
        )

        content.addLayout(
            middle,
            2
        )

        content.addLayout(
            right,
            1
        )


        main.addLayout(
            content
        )



        self.search.textChanged.connect(
            self.load_modules
        )


        self.refresh_btn.clicked.connect(
            self.load_modules
        )


        self.load_modules()



    def load_modules(self):

        self.all_modules.clear()


        folder = (
            BASE_DIR /
            "modules"
        )


        if folder.exists():

            for item in folder.iterdir():

                if item.is_dir() and item.name != "__pycache__":

                    self.all_modules[item.name] = item



        self.modules.clear()


        text = (
            self.search.text()
            .lower()
        )


        for name in sorted(
            self.all_modules
        ):

            if text in name.lower():

                self.modules.addItem(
                    "✅ " + name
                )



        self.status.setText(
            f"🟢 Online | 📦 Moduuleita: {len(self.all_modules)}"
        )



    def select_module(self, item):

        name = (
            item.text()
            .replace(
                "✅ ",
                ""
            )
        )


        self.current_module = name


        path = self.all_modules[name]


        category = "unknown"

        version = "1.0"


        config = path / "config.json"


        if config.exists():

            try:

                with open(
                    config,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data = json.load(f)


                category = data.get(
                    "category",
                    "unknown"
                )


                version = data.get(
                    "version",
                    "1.0"
                )

            except:

                pass



        self.info.setText(
f"""
🐻 Module Inspector

Nimi:
{name}

📂 Kategoria:
{category}

📌 Versio:
{version}

🟢 Tila:
Ready
"""
        )



    def open_folder(self):

        if self.current_module:

            os.startfile(
                self.all_modules[
                    self.current_module
                ]
            )



app = QApplication(sys.argv)

window = BearCoreStudio()

window.show()

sys.exit(
    app.exec()
)