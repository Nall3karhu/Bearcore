from pathlib import Path

# BearCoren projektin juuri
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def project_path(*paths):
    """
    Muodostaa polun BearCore-projektin juureen.

    Esimerkkejä:
        project_path("config.py")
        project_path("modules", "weather")
    """

    return PROJECT_ROOT.joinpath(*paths)