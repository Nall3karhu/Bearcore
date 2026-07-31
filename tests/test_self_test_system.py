from modules.self_test_system.self_test_system import self_test_system


def test_self_test_system():

    assert self_test_system() == True
