from modules.context_controller.context import (
    add_context,
    get_last_context,
    clear_context,
    context_status
)



def test_context_add():

    clear_context()


    result = add_context(
        "etsi tietoa",
        "3D tulostimet"
    )


    assert result["command"] == "etsi tietoa"

    assert result["topic"] == "3D tulostimet"



def test_context_last():

    clear_context()


    add_context(
        "testi",
        "BearCore"
    )


    result = get_last_context()


    assert result["command"] == "testi"

    assert result["topic"] == "BearCore"



def test_context_status():

    clear_context()


    add_context(
        "status",
        "järjestelmä"
    )


    result = context_status()


    assert result["controller"] == "online"

    assert result["entries"] == 1