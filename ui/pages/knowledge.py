from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QTextEdit,
    QLineEdit
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


        self.layout = QVBoxLayout(
            self
        )


        self.title = QLabel(
            "🐻 BearCore Knowledge"
        )

        self.layout.addWidget(
            self.title
        )


        self.search_box = QLineEdit()

        self.search_box.setPlaceholderText(
            "🔎 Hae muistista..."
        )

        self.layout.addWidget(
            self.search_box
        )


        self.list = QListWidget()

        self.layout.addWidget(
            self.list
        )


        self.info = QTextEdit()

        self.info.setReadOnly(
            True
        )

        self.layout.addWidget(
            self.info
        )


        self.refresh = QPushButton(
            "🔄 Päivitä"
        )

        self.layout.addWidget(
            self.refresh
        )


        self.refresh.clicked.connect(
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


        data = load_knowledge()


        for item in data:

            self.list.addItem(
                item["topic"]
            )



    def search(self):

        text = self.search_box.text()


        self.list.clear()


        if text == "":

            self.load_data()

            return



        results = search_knowledge(
            text
        )


        for item in results:

            self.list.addItem(
                item["topic"]
            )



    def show_info(self, item):

        results = search_knowledge(
            item.text()
        )


        if results:

            data = results[0]


            self.info.setText(
f"""
📌 {data['topic']}

📝 {data['content']}

📂 Lähde:
{data['source']}

🕒 Aika:
{data['time']}
"""
            )