import os


def create_ui(args):

    if len(args) == 0:
        print("Käyttö: developer new ui <nimi>")
        return

    name = args[0].lower()

    ui_path = "ui"

    if os.path.exists(ui_path):
        print("⚠️ ui-kansio löytyy jo. Lisätään puuttuvat tiedostot.")
    else:
        os.makedirs(ui_path)

    pages_path = os.path.join(ui_path, "pages")

    os.makedirs(pages_path, exist_ok=True)

    files = {

        f"{name}.py":
f'''import customtkinter as ctk


class {name.capitalize()}App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("BearCore {name}")
        self.geometry("1200x700")

        label = ctk.CTkLabel(
            self,
            text="🐻 BearCore {name}",
            font=("Arial", 28)
        )

        label.pack(pady=30)


if __name__ == "__main__":

    app = {name.capitalize()}App()
    app.mainloop()
''',

        "theme.py":
'''import customtkinter as ctk


def setup_theme():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
''',

        "sidebar.py":
'''def sidebar():

    print("BearCore sidebar")
'''
    }


    pages = [
        "dashboard",
        "assistant",
        "planner",
        "developer"
    ]


    for filename, content in files.items():

        path = os.path.join(ui_path, filename)

        if not os.path.exists(path):

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"✅ Luotu {path}")


    for page in pages:

        path = os.path.join(
            pages_path,
            f"{page}.py"
        )

        if not os.path.exists(path):

            with open(path, "w", encoding="utf-8") as f:

                f.write(
f'''def show():

    print("{page} page")
'''
                )

            print(f"✅ Luotu page: {page}")


    print("\n🐻 BearCore UI valmis!")