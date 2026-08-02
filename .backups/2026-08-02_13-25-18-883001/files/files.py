from modules.files.router import route


def files(args=None):
    """
    Files-moduulin pääsisäänkäynti.
    Sallii kutsun sekä ilman argumentteja että argumenttien kanssa.
    """

    if args is None:
        args = []

    return route(args)