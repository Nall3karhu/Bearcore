from modules.learning_controller.learning import (
    learn,
    search_learning,
    learning_status
)


def test_learning_save():

    result = learn(
        "Testi",
        "Learning Controller toimii"
    )

    assert result["topic"] == "Testi"



def test_learning_search():

    result = search_learning(
        "Testi"
    )

    assert len(result) > 0



def test_learning_status():

    result = learning_status()

    assert result["controller"] == "online"