import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.pages.bearcore_console import BearCoreConsolePage



class BearCoreApp(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "🐻 BearCore"
        )

        self.resize(
            900,
            600
        )


        self.console = BearCoreConsolePage()

        self.setCentralWidget(
            self.console
        )



def main():

    app = QApplication(
        sys.argv
    )


    window = BearCoreApp()

    window.show()


    sys.exit(
        app.exec()
    )



if __name__ == "__main__":

    main()