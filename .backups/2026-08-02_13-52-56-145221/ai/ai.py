from core.memory import save_memory, load_memory


def ai(args=None):

    print("\n======================")
    print("BearCore AI")
    print("======================")

    while True:

        user = input("Sinä > ").strip()

        if user.lower() in ["poistu", "exit", "lopeta"]:
            print("AI suljetaan.")
            break

        # Muista...
        if user.lower().startswith("muista "):

            teksti = user[7:]

            if "=" in teksti:

                key, value = teksti.split("=", 1)

                save_memory(key.strip(), value.strip())

                print("🧠 Tallennettu muistiin.")

            else:

                print("Kirjoita muodossa:")
                print("muista nimi = BearCore")

            continue

        # Mikä on...
        if user.lower().startswith("mikä on "):

            key = user[8:].strip()

            result = load_memory(key)

            if result:

                print(f"🧠 {key} = {result}")

            else:

                print("En tiedä vielä.")

            continue

        print("🤖 Ymmärsin viestin, mutta en vielä osaa vastata siihen.")