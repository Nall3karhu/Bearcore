from datetime import datetime



def create_report(
    title,
    data
):

    return {

        "time":
            datetime.now().isoformat(),

        "title":
            title,

        "data":
            data

    }



def generate(
    title,
    data
):

    return {

        "success":
            True,

        "report":
            create_report(
                title,
                data
            )

    }



def summary(
    data
):

    return {

        "success":
            True,

        "summary":
            str(data)

    }