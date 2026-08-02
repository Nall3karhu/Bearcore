from pathlib import Path



def scan_folder(
    folder
):

    path = Path(
        folder
    )


    if not path.exists():

        return []


    files = []


    for file in path.rglob("*"):

        if file.is_file():

            files.append(
                str(file)
            )


    return files



def read_text(
    file
):

    path = Path(
        file
    )


    if not path.exists():

        return None


    try:

        return path.read_text(
            encoding="utf-8"
        )

    except:

        return None



def import_data(
    source
):

    return {

        "success": True,

        "source":
            source,

        "message":
            "📥 Data valmis käsittelyyn"

    }