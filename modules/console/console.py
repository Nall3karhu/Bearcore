from datetime import datetime

from modules.core_kernel.kernel import boot
from modules.startup_manager.startup import startup
from modules.health_monitor.health import health



def create_response(
    command,
    result
):

    return {

        "time":
            datetime.now().isoformat(),

        "command":
            command,

        "result":
            result

    }



def get_commands():

    return [

        "status",

        "health",

        "boot",

        "backup",

        "test",

        "modules",

        "help"

    ]



def run_backup():

    return {

        "success":
            True,

        "message":
            "🐻 Backup Manager valmis",

        "status":
            "ready"

    }



def run_test():

    return {

        "success":
            True,

        "message":
            "🐻 Testijärjestelmä valmis",

        "status":
            "ready"

    }



def run_modules():

    return {

        "success":
            True,

        "message":
            "Moduulien tarkistus valmis",

        "status":
            "ready"

    }



def execute(
    command
):

    command = command.lower().strip()



    if command == "help":

        return create_response(

            command,

            get_commands()

        )



    if command == "status":

        return create_response(

            command,

            startup()

        )



    if command == "health":

        return create_response(

            command,

            health()

        )



    if command == "boot":

        return create_response(

            command,

            boot()

        )



    if command == "backup":

        return create_response(

            command,

            run_backup()

        )



    if command == "test":

        return create_response(

            command,

            run_test()

        )



    if command == "modules":

        return create_response(

            command,

            run_modules()

        )



    return create_response(

        command,

        "Tuntematon komento"

    )



def start_console():

    print(
        "🐻 BearCore Console"
    )

    print(
        "Kirjoita help nähdäksesi komennot"
    )


    while True:

        command = input(
            "\n> "
        )


        if command == "exit":

            break


        print(
            execute(command)
        )