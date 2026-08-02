from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QLineEdit,
    QTextEdit
)

from core.knowledge_manager import (
    load_knowledge,
    search_knowledge
)



class KnowledgePage(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "📚 BearCore Knowledge"
        )


        self.resize(
            700,
            600
        )


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            QLabel(
                "🐻 BearCore Knowledge"
            )
        )


        self.search_box = QLineEdit()

        self.search_box.setPlaceholderText(
            "🔎 Hae muistista..."
        )


        layout.addWidget(
            self.search_box
        )


        self.list = QListWidget()

        layout.addWidget(
            self.list
        )


        self.info = QTextEdit()

        self.info.setReadOnly(
            True
        )

        layout.addWidget(
            self.info
        )


        self.refresh_btn = QPushButton(
            "🔄 Päivitä"
        )

        layout.addWidget(
            self.refresh_btn
        )


        self.refresh_btn.clicked.connect(
            self.load_data
        )


        self.search_box.textChanged.connect(
            self.search
        )


        self.list.itemClicked.connect(
            self.show_info
        )


        self.load_data()



    def load_data(self):

        self.list.clear()


        for item in load_knowledge():

            self.list.addItem(
                item["topic"]
            )



    def search(self):

        text = self.search_box.text()


        self.list.clear()


        if not text:

            self.load_data()

            return


        for item in search_knowledge(text):

            self.list.addItem(
                item["topic"]
            )



    def show_info(self, item):

        result = search_knowledge(
            item.text()
        )


        if result:

            data = result[0]


            self.info.setText(
f"""
📌 {data['topic']}

📝 {data['content']}

🕒 {data['time']}
"""
            )