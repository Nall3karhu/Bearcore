from launcher import start


def test_launcher():

    result = start()

    assert result["status"] == "online"

    assert result["kernel"]["success"] is True

    assert result["startup"]["success"] is True

    assert result["health"]["success"] is True