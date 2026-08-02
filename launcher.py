from modules.startup_manager.startup import startup
from modules.health_monitor.health import health
from modules.core_kernel.kernel import boot
from modules.logging_manager.logger import info


def start():

    info(
        "BearCore käynnistys alkoi",
        "launcher"
    )

    kernel = boot()

    system = startup()

    health_check = health()

    return {

        "kernel": kernel,

        "startup": system,

        "health": health_check,

        "status": "online"

    }


if __name__ == "__main__":

    result = start()

    print(
        "🐻 BearCore ONLINE"
    )

    print(
        result
    )