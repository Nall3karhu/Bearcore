import customtkinter as ctk


class DesktopApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("BearCore desktop")
        self.geometry("1200x700")

        label = ctk.CTkLabel(
            self,
            text="🐻 BearCore desktop",
            font=("Arial", 28)
        )

        label.pack(pady=30)


if __name__ == "__main__":

    app = DesktopApp()
    app.mainloop()
