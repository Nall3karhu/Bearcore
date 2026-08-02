from pathlib import Path
import os
import subprocess
import json

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
)


class ModuleInfoPage(QWidget):

    def __init__(self, module_name):

        super().__init__()

        self.module_name = module_name

        self.setWindowTitle(
            "🐻 BearCore Module Inspector"
        )

        self.resize(
            700,
            700
        )


        layout = QVBoxLayout(self)


        self.title = QLabel()
        self.category = QLabel()
        self.version = QLabel()
        self.status = QLabel()


        layout.addWidget(self.title)
        layout.addWidget(self.category)
        layout.addWidget(self.version)
        layout.addWidget(self.status)


        self.info = QTextEdit()

        self.info.setReadOnly(True)

        layout.addWidget(self.info)


        # Toiminnot

        self.analyze_btn = QPushButton(
            "🔍 Analyze"
        )

        self.test_btn = QPushButton(
            "🧪 Test"
        )

        self.backup_btn = QPushButton(
            "💾 Backup"
        )

        self.repair_btn = QPushButton(
            "🛠 Repair"
        )

        self.reload_btn = QPushButton(
            "🔄 Reload"
        )

        self.open_btn = QPushButton(
            "📂 Avaa kansio"
        )


        layout.addWidget(self.analyze_btn)
        layout.addWidget(self.test_btn)
        layout.addWidget(self.backup_btn)
        layout.addWidget(self.repair_btn)
        layout.addWidget(self.reload_btn)
        layout.addWidget(self.open_btn)


        self.analyze_btn.clicked.connect(
            self.analyze_module
        )

        self.test_btn.clicked.connect(
            self.test_module
        )

        self.backup_btn.clicked.connect(
            self.backup_module
        )

        self.repair_btn.clicked.connect(
            self.repair_module
        )

        self.reload_btn.clicked.connect(
            self.reload_module
        )

        self.open_btn.clicked.connect(
            self.open_folder
        )


        self.load_info()



    def find_bearcore(self):

        current = Path(__file__).resolve()

        for parent in current.parents:

            if parent.name == "BearCore":

                return parent

        return None



    def module_path(self):

        base = self.find_bearcore()

        if not base:

            return None

        return (
            base /
            "modules" /
            self.module_name
        )



    def load_info(self):

        path = self.module_path()


        self.title.setText(
            f"🐻 Moduuli: {self.module_name}"
        )


        if not path or not path.exists():

            self.status.setText(
                "🔴 Moduulia ei löytynyt"
            )

            return


        config = path / "config.json"

        data = {}


        if config.exists():

            try:

                with open(
                    config,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data = json.load(f)

            except:

                pass



        self.category.setText(
            f"📂 Kategoria: {data.get('category','unknown')}"
        )

        self.version.setText(
            f"📌 Versio: {data.get('version','1.0')}"
        )


        self.status.setText(
            "🟢 Tila: valmis"
        )


        text = []

        text.append("⚙ Config:")

        text.append(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False
            )
        )


        text.append("\n📄 Tiedostot:")


        for file in path.rglob("*"):

            if file.is_file():

                text.append(
                    str(
                        file.relative_to(path)
                    )
                )


        self.info.setText(
            "\n".join(text)
        )



    def analyze_module(self):

        self.status.setText(
            "🔍 Analyze käynnissä..."
        )



    def test_module(self):

        self.status.setText(
            "🧪 Testi käynnissä..."
        )



    def backup_module(self):

        self.status.setText(
            "💾 Backup käynnissä..."
        )



    def repair_module(self):

        self.status.setText(
            "🛠 Repair käynnissä..."
        )



    def reload_module(self):

        try:

            from core.module_manager import reload_modules

            reload_modules()


            self.status.setText(
                "🟢 Moduulit ladattu"
            )


        except Exception as e:

            self.status.setText(
                f"❌ {e}"
            )



    def open_folder(self):

        path = self.module_path()


        if path and path.exists():

            os.startfile(path)