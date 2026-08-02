import os


PLUGIN_PATH = "modules/developer/commands"



def list_plugins(args=None):

    print("\n🐻 BearCore Plugins")
    print("=" * 35)


    if not os.path.exists(PLUGIN_PATH):

        print("❌ Plugin-kansiota ei löydy.")
        return


    plugins = []


    for file in os.listdir(PLUGIN_PATH):

        if file.endswith(".py"):

            if file not in [
                "__init__.py",
                "loader.py"
            ]:

                plugins.append(
                    file[:-3]
                )


    for plugin in sorted(plugins):

        print(
            f"✅ {plugin}"
        )


    print(
        f"\nPlugin määrä: {len(plugins)}"
    )



def remove_plugin(args=None):

    if not args:

        print(
            "❌ Käyttö: developer remove plugin <nimi>"
        )

        return


    name = args[-1]


    path = os.path.join(
        PLUGIN_PATH,
        f"{name}.py"
    )


    if not os.path.exists(path):

        print(
            "❌ Pluginia ei löytynyt."
        )

        return


    os.remove(path)


    print(
        f"🗑️ Poistettu plugin: {name}"
    )