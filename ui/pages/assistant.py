from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QLineEdit,
    QPushButton
)


from modules.assistant_orchestrator.orchestrator import ask


from modules.assistant_learning.integration import (
    process_learning_conversation
)


from modules.response_formatter.cleaner import (
    clean_research_response
)



class AssistantPage(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "🐻 BearCore Assistant"
        )


        self.resize(
            800,
            600
        )


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            QLabel(
                "🐻 BearCore Assistant"
            )
        )


        self.chat = QTextEdit()

        self.chat.setReadOnly(
            True
        )


        layout.addWidget(
            self.chat
        )


        self.input = QLineEdit()


        self.input.setPlaceholderText(
            "Kirjoita viesti..."
        )


        layout.addWidget(
            self.input
        )


        self.send_button = QPushButton(
            "▶ Lähetä"
        )


        layout.addWidget(
            self.send_button
        )


        self.send_button.clicked.connect(
            self.send_message
        )


        self.input.returnPressed.connect(
            self.send_message
        )


        self.chat.append(
            "🐻 BearCore valmis."
        )



    def send_message(
        self
    ):

        message = self.input.text()


        if not message:

            return



        self.chat.append(

            "\nSinä:\n" + message

        )



        try:


            result = ask(
                message
            )


            if (

                isinstance(result, dict)

                and "analysis" in result.get(
                    "data",
                    {}
                )

            ):

                response = clean_research_response(
                    result
                )


            else:

                response = str(
                    result
                )



            process_learning_conversation(

                message,

                response

            )


            self.chat.append(

                "\n🐻 BearCore:\n"

                +

                response

            )



        except Exception as e:


            self.chat.append(

                "\n❌ Virhe:\n"

                +

                str(e)

            )



        self.input.clear()