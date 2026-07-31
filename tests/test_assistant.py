from modules.assistant.assistant import assistant
from unittest.mock import patch


def test_assistant():
    with patch("builtins.input", side_effect=["poistu"]):
        assistant()