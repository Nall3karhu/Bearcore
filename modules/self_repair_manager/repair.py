from datetime import datetime



def create_response(
    success,
    action,
    message,
    data=None
):

    return {

        "success":
            success,

        "time":
            datetime.now().isoformat(),

        "action":
            action,

        "message":
            message,

        "data":
            data

    }



def analyze_problem(
    problem
):

    if not problem:

        return create_response(

            False,

            "analyze",

            "Ongelma puuttuu"

        )



    return create_response(

        True,

        "analyze",

        "🔎 Ongelma analysoitu",

        {

            "problem":
                problem,

            "solution":
                "pending"

        }

    )



def create_fix(
    problem,
    solution
):

    return {

        "problem":
            problem,

        "solution":
            solution,

        "status":
            "ready"

    }



def execute_fix(
    fix
):

    if not fix:

        return create_response(

            False,

            "repair",

            "Korjausta ei löytynyt"

        )



    fix["status"] = "completed"



    return create_response(

        True,

        "repair",

        "🛠 Korjaus suoritettu",

        fix

    )



def repair_from_test(
    test_result
):

    if not test_result:

        return create_response(

            False,

            "repair",

            "Testitulosta ei saatu"

        )



    return create_response(

        True,

        "repair",

        "🔧 Korjausprosessi valmis",

        {

            "source":
                "self_test",

            "result":
                test_result

        }

    )



def repair_status():

    return {

        "manager":
            "online",

        "mode":
            "ready"

    }