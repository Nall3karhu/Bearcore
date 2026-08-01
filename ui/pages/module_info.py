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
            "🐻 BearCore Module Info"
        )

        self.resize(
            600,
            600
        )


        layout = QVBoxLayout(
            self
        )


        self.title = QLabel()

        self.category = QLabel()

        self.version = QLabel()

        self.status = QLabel()


        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.category
        )

        layout.addWidget(
            self.version
        )

        layout.addWidget(
            self.status
        )


        self.files = QTextEdit()

        self.files.setReadOnly(
            True
        )

        layout.addWidget(
            self.files
        )


        self.open_btn = QPushButton(
            "📂 Avaa kansio"
        )

        self.reload_btn = QPushButton(
            "🔄 Reload"
        )

        self.start_btn = QPushButton(
            "▶ Käynnistä moduuli"
        )

        self.refresh_btn = QPushButton(
            "🔄 Päivitä tiedot"
        )


        layout.addWidget(
            self.open_btn
        )

        layout.addWidget(
            self.reload_btn
        )

        layout.addWidget(
            self.start_btn
        )

        layout.addWidget(
            self.refresh_btn
        )


        self.open_btn.clicked.connect(
            self.open_folder
        )

        self.reload_btn.clicked.connect(
            self.reload_module
        )

        self.start_btn.clicked.connect(
            self.start_module
        )

        self.refresh_btn.clicked.connect(
            self.load_info
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



        config = (
            path /
            "config.json"
        )


        category = "unknown"

        version = "1.0"



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



        self.category.setText(
            f"📂 Kategoria: {category}"
        )


        self.version.setText(
            f"📌 Versio: {version}"
        )


        self.status.setText(
            "🟢 Tila: valmis"
        )



        files = []


        for file in path.rglob("*"):

            if file.is_file():

                files.append(
                    str(
                        file.relative_to(path)
                    )
                )


        self.files.setText(
            "📄 Tiedostot:\n\n" +
            "\n".join(files)
        )



    def open_folder(self):

        path = self.module_path()


        if path and path.exists():

            os.startfile(
                path
            )



    def reload_module(self):

        try:

            from core.module_manager import reload_modules

            reload_modules()


            self.status.setText(
                "🟢 Moduulit ladattu uudelleen"
            )


        except Exception as e:

            self.status.setText(
                f"❌ {e}"
            )



    def start_module(self):

        path = self.module_path()


        if not path:

            return


        main_file = (
            path /
            "module.py"
        )


        if main_file.exists():

            subprocess.Popen(
                [
                    "python",
                    str(main_file)
                ]
            )


            self.status.setText(
                "🟢 Moduuli käynnistetty"
            )

        else:

            self.status.setText(
                "⚠️ module.py puuttuu"
            )