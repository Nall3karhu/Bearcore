from core.module_registry import get


def command(args):

    if len(args) < 2:
        return False

    if args[0] != "info":
        return False

    name = args[1]

    module = get(name)

    if module is None:

        print(f"❌ Moduulia '{name}' ei löytynyt.")
        return True

    print("")
    print("📦 Module Information")
    print("-" * 40)

    print(f"Nimi:        {module['name']}")
    print(f"Versio:      {module['version']}")
    print(f"Kategoria:   {module['category']}")

    aliases = module.get("aliases", [])

    if aliases:
        print(f"Alias:       {', '.join(aliases)}")
    else:
        print("Alias:       -")

    description = module.get("description", "")

    if description:
        print(f"Kuvaus:      {description}")
    else:
        print("Kuvaus:      -")

    print("-" * 40)

    return True