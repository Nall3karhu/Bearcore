import webbrowser
from urllib.parse import quote


def browser(args=None):

    if args is None:
        args = []

    if len(args) == 0:
        print("""
=========================
BearCore Browser
=========================

Käyttö:
browser <hakusana>

Esimerkki:
browser python sqlite
""")
        return

    query = " ".join(args)

    url = f"https://www.google.com/search?q={quote(query)}"

    print(f"🌐 Haetaan: {query}")

    webbrowser.open(url)