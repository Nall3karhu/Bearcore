from modules.weather.weather import weather

# BearCoren moduulit
MODULES = {
    "sää": weather,
}


def run_module(command):
    if command in MODULES:
        MODULES[command]()
        return True

    return False