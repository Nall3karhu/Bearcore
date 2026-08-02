from modules.response_formatter.formatter import (
    format_response,
    formatter_status
)



def test_formatter_message():

    result = format_response(

        {

            "message":
                "BearCore online",

            "data":
                {

                    "Kernel":
                        "ready"

                }

        }

    )


    assert "BearCore online" in result

    assert "Kernel" in result



def test_formatter_string():

    result = format_response(
        "testi"
    )


    assert result == "testi"



def test_formatter_status():

    result = formatter_status()


    assert result["status"] == "ready"