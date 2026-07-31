from modules.github.github import github
from unittest.mock import patch


def test_github():
    with patch("builtins.input", side_effect=["3"]):
        github()