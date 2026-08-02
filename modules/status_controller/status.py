from datetime import datetime



def create_status_response():

    return {

        "success": True,

        "time":
            datetime.now().isoformat(),

        "message":
            "Järjestelmä online",

        "components":

            [

                {

                    "name":
                        "Kernel",

                    "status":
                        "ready"

                },

                {

                    "name":
                        "Modules",

                    "status":
                        "ready"

                },

                {

                    "name":
                        "Controllers",

                    "status":
                        "ready"

                },

                {

                    "name":
                        "Health",

                    "status":
                        "ready"

                }

            ]

    }



def format_status():

    data = create_status_response()


    lines = []


    lines.append(
        "🐻 BearCore:"
    )


    lines.append(
        ""
    )


    lines.append(

        "Järjestelmä online ✅"

    )


    lines.append(
        ""
    )


    lines.append(
        "Komponentit:"
    )


    for component in data["components"]:

        lines.append(

            f"✅ {component['name']}"

        )


    return "\n".join(
        lines
    )



def status_controller():

    return {

        "module":
            "status_controller",

        "status":
            "ready"

    }