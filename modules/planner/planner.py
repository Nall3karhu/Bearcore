import json
import os


def developer(args):

    if len(args) == 0:
        print("""
=========================
BearCore Developer
=========================

Komennot:

developer status
developer new module <nimi>
""")
        return

    if args[0] == "status":
        print("🛠️ Developer toimii.")
        return

    if len(args) < 3:
        print("Käyttö: developer new module <nimi>")
        return

    if args[0] != "new" or args[1] != "module":
        print("Tuntematon developer-komento.")
        return

    nimi = args[2].lower()

    module_folder = os.path.join("modules", nimi)

    if os.path.exists(module_folder):
        print("❌ Moduuli on jo olemassa.")
        return

    print("\n=== Uuden moduulin asetukset ===")

    kuvaus = input("Kuvaus: ").strip()

    testi = input("Luodaanko testi? (k/e): ").lower() == "k"
    docs = input("Luodaanko dokumentaatio? (k/e): ").lower() == "k"

    os.makedirs(module_folder, exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    os.makedirs("tests", exist_ok=True)

    # __init__.py
    open(os.path.join(module_folder, "__init__.py"), "w").close()

    # config.json
    config = {
        "name": nimi,
        "description": kuvaus,
        "version": "1.0"
    }

    with open(os.path.join(module_folder, "config.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    # README
    with open(os.path.join(module_folder, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"""# {nimi}

{kuvaus}

## Komento

{nimi}
""")

    # Python-tiedosto
    with open(os.path.join(module_folder, f"{nimi}.py"), "w", encoding="utf-8") as f:
        f.write(f'''def {nimi}(args=None):

    print("✅ {nimi}-moduuli toimii!")
''')

    # Testi
    if testi:
        with open(os.path.join("tests", f"test_{nimi}.py"), "w", encoding="utf-8") as f:
            f.write(f'''from modules.{nimi}.{nimi} import {nimi}


def test_{nimi}():
    {nimi}()
''')

    # Dokumentaatio
    if docs:
        with open(os.path.join("docs", f"{nimi}.md"), "w", encoding="utf-8") as f:
            f.write(f"""# {nimi}

## Kuvaus

{kuvaus}

## TODO

- Toteuta moduuli
""")

    print("\n==============================")
    print("✅ Moduuli luotu onnistuneesti")
    print("==============================")
    print(f"Nimi: {nimi}")
    print(f"Kuvaus: {kuvaus}")
    print(f"Kansio: modules/{nimi}")

    if testi:
        print("✅ Testi luotu")

    if docs:
        print("✅ Dokumentaatio luotu")

    print("\nℹ️ Käynnistä BearCore uudelleen.")