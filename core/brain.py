from core.parser import parse
from core.module_manager import run_module
from core.memory import save_memory, load_memory


class Brain:

    def think(self, command):

        result = parse(command)

        intent = result["intent"]

        if intent == "module":

            if not run_module(command):
                print("❌ Moduulia ei löytynyt.")

            return

        if intent == "save":

            teksti = result["text"]

            osat = teksti.split()

            if len(osat) >= 3:

                key = osat[1]
                value = " ".join(osat[2:])

                save_memory(key, value)

                print(f"🧠 Tallennettu: {key}")

            else:

                print("Käyttö: muista <avain> <tieto>")

            return

        if intent == "search":

            osat = result["text"].split()

            if len(osat) >= 2:

                key = osat[1]

                value = load_memory(key)

                if value:
                    print(f"🧠 {key} = {value}")
                else:
                    print("Tietoa ei löytynyt.")

            return

        print("🤖 En ymmärtänyt komentoa.")