import os


def create_plan(args=None):

    if not args:

        print("❌ Käyttö: developer plan module <nimi>")
        return


    name = args[-1].lower()


    print("\n🐻 BearCore Code Planner")
    print("=" * 35)


    print(f"""
Moduuli:
{name}


Suunnitelma:

📁 modules/{name}

├── {name}.py
├── __init__.py
├── config.json
└── README.md


Testit:

✅ tests/test_{name}.py


Vaiheet:

1. Luo rakenne
2. Luo Python-moduuli
3. Lisää asetukset
4. Luo testi
5. Aja testit


🟢 Suunnitelma valmis.
""")