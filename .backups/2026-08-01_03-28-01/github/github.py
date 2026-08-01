import subprocess


def github(args=None):

    print("\n=== GitHub ===")
    print("1. Git status")
    print("2. Viimeiset commitit")
    print("3. Takaisin")

    valinta = input("Valinta: ")

    if valinta == "1":
        subprocess.run(["git", "status"])

    elif valinta == "2":
        subprocess.run(["git", "log", "--oneline", "-5"])