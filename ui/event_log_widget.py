from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
)

from PySide6.QtCore import QTimer

from core.event_logger import get_events



class EventLogWidget(QWidget):

    def __init__(self):

        super().__init__()


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            QLabel(
                "📜 BearCore Event Log"
            )
        )


        self.log_view = QTextEdit()

        self.log_view.setReadOnly(
            True
        )


        layout.addWidget(
            self.log_view
        )


        self.refresh_btn = QPushButton(
            "🔄 Päivitä loki"
        )


        layout.addWidget(
            self.refresh_btn
        )


        self.refresh_btn.clicked.connect(
            self.refresh
        )


        self.timer = QTimer()

        self.timer.timeout.connect(
            self.refresh
        )


        self.timer.start(
            3000
        )


        self.refresh()



    def refresh(self):

        self.log_view.clear()


        try:

            events = get_events()

        except Exception:

            events = []



        if not events:

            self.log_view.setText(
                "Ei tapahtumia vielä."
            )

            return



        for event in reversed(events[-50:]):


            self.log_view.append(

f"""
🕒 {event.get("time")}

{event.get("event")}

------------------------
"""
            )