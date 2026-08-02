from pathlib import Path
from datetime import datetime
import subprocess



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def create_result(
    name,
    status,
    message=""
):

    return {

        "name":
            name,

        "status":
            status,

        "message":
            message

    }



def check_folder(
    name
):

    base = find_bearcore()


    if not base:

        return create_result(

            name,

            False,

            "BearCore ei löytynyt"

        )



    path = (
        base /
        name
    )


    if path.exists():

        return create_result(

            name,

            True,

            "OK"

        )


    return create_result(

        name,

        False,

        "Puuttuu"

    )



def check_modules():

    return check_folder(
        "modules"
    )



def check_config():

    return check_folder(
        "config"
    )



def check_tests():

    return check_folder(
        "tests"
    )



def run_pytest():

    try:

        result = subprocess.run(

            [

                "python",

                "-m",

                "pytest"

            ],

            capture_output=True,

            text=True,

            timeout=120

        )


        return {

            "success":

                result.returncode == 0,

            "output":

                result.stdout[-1000:]

        }


    except Exception as e:


        return {

            "success":
                False,

            "output":
                str(e)

        }



def run_self_test():

    checks = [

        check_modules(),

        check_config(),

        check_tests()

    ]


    tests = run_pytest()



    return {

        "time":
            datetime.now().isoformat(),

        "checks":
            checks,

        "pytest":
            tests,

        "status":

            "healthy"

            if tests["success"]

            else

            "warning"

    }



def status():

    return {

        "manager":
            "online",

        "purpose":
            "system checking"

    }