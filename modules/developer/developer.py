import os


def developer(args):

    if len(args) == 0:
        print("""
=========================
BearCore Developer
=========================

developer status
developer new module <nimi>
""")
        return

    if args[0] == "status":
        print("🛠️ Developer toimii.")
        return

    if args[0] != "new":
        print("Tuntematon developer-komento.")
        return

    if len(args) < 3:
        print("Käyttö: developer new module <nimi>")
        return

    if args[1] != "module":
        print("Tuntematon kohde.")
        return

    nimi = args[2].lower()

    module_folder = os.path.join("modules", nimi)

    if os.path.exists(module_folder):
        print("❌ Moduuli on jo olemassa.")
        return

    # Luodaan kansiot
    os.makedirs(module_folder, exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    os.makedirs("tests", exist_ok=True)

    # __init__.py
    with open(os.path.join(module_folder, "__init__.py"), "w", encoding="utf-8") as f:
        pass

    # config.json
    with open(os.path.join(module_folder, "config.json"), "w", encoding="utf-8") as f:
        f.write("{}")

    # README.md
    with open(os.path.join(module_folder, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"""# {nimi}

BearCore-moduuli.

## Komento

{nimi}
""")

    # Python-moduuli
    with open(os.path.join(module_folder, f"{nimi}.py"), "w", encoding="utf-8") as f:
        f.write(f'''def {nimi}(args=None):
    print("✅ {nimi}-moduuli toimii!")
''')

    # Testi
    with open(os.path.join("tests", f"test_{nimi}.py"), "w", encoding="utf-8") as f:
        f.write(f'''from modules.{nimi}.{nimi} import {nimi}


def test_{nimi}():
    {nimi}()
''')

    # Dokumentaatio
    with open(os.path.join("docs", f"{nimi}.md"), "w", encoding="utf-8") as f:
        f.write(f"""# {nimi}

Tämän moduulin dokumentaatio.

## Tarkoitus

TODO
""")

    print()
    print("=========================")
    print("✅ Moduuli luotu")
    print("=========================")
    print(f"Nimi: {nimi}")
    print(f"Kansio: modules/{nimi}")
    print("README: OK")
    print("config.json: OK")
    print("Python-tiedosto: OK")
    print("Testi: OK")
    print("Dokumentaatio: OK")
    print()
    print("ℹ️ Käynnistä BearCore uudelleen.")
    print("Moduuli latautuu automaattisesti.")