from pathlib import Path
import os
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
            f"🐻 Nimi: {self.module_name}"
        )


        if not path or not path.exists():

            self.status.setText(
                "🔴 Moduulia ei löytynyt"
            )

            return



        config_data = {}


        config = (
            path /
            "config.json"
        )


        if config.exists():

            try:

                with open(
                    config,
                    "r",
                    encoding="utf-8"
                ) as f:

                    config_data = json.load(f)

            except:

                config_data = {}



        self.category.setText(
            f"📂 Kategoria: {config_data.get('category','unknown')}"
        )


        self.version.setText(
            f"📌 Versio: {config_data.get('version','1.0')}"
        )


        self.status.setText(
            "🟢 Tila: Ready"
        )



        output = []


        output.append(
            "⚙ Config:"
        )


        output.append(
            json.dumps(
                config_data,
                indent=4,
                ensure_ascii=False
            )
        )



        output.append(
            ""
        )

        output.append(
            "📄 Tiedostot:"
        )


        for file in path.rglob("*"):

            if file.is_file():

                output.append(
                    str(
                        file.relative_to(path)
                    )
                )


        self.info.setText(
            "\n".join(output)
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

            os.startfile(
                path
            )