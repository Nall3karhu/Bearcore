from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
)

from core.event_logger import get_events



class EventLogWidget(QWidget):

    def __init__(self):

        super().__init__()


        layout = QVBoxLayout(
            self
        )


        self.title = QLabel(
            "📜 BearCore Event Log"
        )


        self.log = QTextEdit()

        self.log.setReadOnly(
            True
        )


        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.log
        )


        self.refresh()



    def refresh(self):

        self.log.clear()


        events = get_events()


        if not events:

            self.log.setText(
                "Ei tapahtumia vielä."
            )

            return



        for event in reversed(events):

            self.log.append(
                f"""
{event['time']}
{event['event']}

--------------------
"""
            )