import sys
import os

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


from ui.dashboard_panel import DashboardPanel
from ui.event_log_widget import EventLogWidget

from core.logger import log



class BearCoreStudio(QMainWindow):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "🐻 BearCore Studio"
        )


        self.resize(
            1400,
            900
        )


        self.windows = {}

        self.all_modules = {}

        self.current_module = None


        central = QWidget()

        self.setCentralWidget(
            central
        )


        main = QVBoxLayout(
            central
        )


        self.dashboard = DashboardPanel()

        main.addWidget(
            self.dashboard
        )


        content = QHBoxLayout()



        # Vasen moduulit

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



        # Keskiosa

        middle = QVBoxLayout()


        middle.addWidget(
            QLabel(
                "🔎 Module Inspector"
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


        middle.addWidget(
            self.open_btn
        )


        self.open_btn.clicked.connect(
            self.open_folder
        )



        # Oikea puoli

        right = QVBoxLayout()


        self.event_log = EventLogWidget()


        right.addWidget(
            self.event_log
        )



        tools = QGroupBox(
            "🐻 BearCore Tools"
        )


        tool_layout = QVBoxLayout()



        self.dashboard_btn = QPushButton(
            "📊 Dashboard"
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

        self.assistant_btn = QPushButton(
            "🐻 Assistant"
        )

        self.knowledge_btn = QPushButton(
            "📚 Knowledge"
        )

        self.console_btn = QPushButton(
            "💻 Console"
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
            self.assistant_btn,
            self.knowledge_btn,
            self.console_btn,
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
            2
        )


        main.addLayout(
            content
        )



        # Napit

        self.dashboard_btn.clicked.connect(
            self.open_dashboard
        )

        self.create_btn.clicked.connect(
            self.open_create
        )

        self.template_btn.clicked.connect(
            self.open_templates
        )

        self.pipeline_btn.clicked.connect(
            self.open_pipeline
        )

        self.report_btn.clicked.connect(
            self.open_reports
        )

        self.assistant_btn.clicked.connect(
            self.open_assistant
        )

        self.knowledge_btn.clicked.connect(
            self.open_knowledge
        )

        self.console_btn.clicked.connect(
            self.open_console
        )

        self.refresh_btn.clicked.connect(
            self.refresh_all
        )


        self.search.textChanged.connect(
            self.load_modules
        )


        log(
            "🐻 BearCore Studio käynnistetty"
        )


        self.load_modules()



    def open_page(
        self,
        name,
        cls
    ):

        if name not in self.windows:

            self.windows[name] = cls()


        self.windows[name].show()



    def open_dashboard(self):

        from ui.pages.dashboard import DashboardPage

        self.open_page(
            "dashboard",
            DashboardPage
        )



    def open_create(self):

        from ui.pages.create_module import CreateModulePage

        self.open_page(
            "create",
            CreateModulePage
        )



    def open_templates(self):

        from ui.pages.template import TemplatePage

        self.open_page(
            "templates",
            TemplatePage
        )



    def open_pipeline(self):

        from ui.pages.pipeline import PipelinePage

        self.open_page(
            "pipeline",
            PipelinePage
        )



    def open_reports(self):

        from ui.pages.reports import ReportPage

        self.open_page(
            "reports",
            ReportPage
        )



    def open_assistant(self):

        from ui.pages.assistant import AssistantPage

        self.open_page(
            "assistant",
            AssistantPage
        )



    def open_knowledge(self):

        from ui.pages.knowledge import KnowledgePage

        self.open_page(
            "knowledge",
            KnowledgePage
        )



    def open_console(self):

        from ui.pages.bearcore_console import BearCoreConsolePage

        self.open_page(
            "console",
            BearCoreConsolePage
        )



    def refresh_all(self):

        self.load_modules()

        self.dashboard.refresh()

        self.event_log.refresh()



    def load_modules(self):

        self.all_modules.clear()


        folder = BASE_DIR / "modules"


        if folder.exists():

            for item in folder.iterdir():

                if item.is_dir() and item.name != "__pycache__":

                    self.all_modules[item.name] = item



        self.modules.clear()


        for name in sorted(
            self.all_modules
        ):

            self.modules.addItem(
                "✅ " + name
            )



    def select_module(
        self,
        item
    ):

        name = item.text().replace(
            "✅ ",
            ""
        )


        self.current_module = name


        self.info.setText(

f"""
🐻 Module Inspector

Nimi:
{name}

Tila:
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



if __name__ == "__main__":

    app = QApplication(
        sys.argv
    )


    window = BearCoreStudio()

    window.show()


    sys.exit(
        app.exec()
    )