from modules.developer.router import route_command


def developer(args=None):
    """
    Developer-moduulin pääsisäänkäynti.
    """

    if args is None:
        args = []

    try:
        return route_command(args)

    except KeyboardInterrupt:
        raise

    except Exception as e:
        print(f"❌ Developer-virhe: {e}")
        return False