from modules.console.console import execute



def test_console_status():

    result = execute(
        "status"
    )

    assert result["command"] == "status"

    assert result["result"]["success"] is True

    assert result["result"]["data"]["status"] == "online"



def test_console_boot():

    result = execute(
        "boot"
    )

    assert result["command"] == "boot"

    assert result["result"]["success"] is True



def test_console_health():

    result = execute(
        "health"
    )

    assert result["command"] == "health"

    assert result["result"]["success"] is True



def test_console_help():

    result = execute(
        "help"
    )

    assert "status" in result["result"]