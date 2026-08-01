from modules.module_validator.module_validator import module_validator


def test_module_validator():

    assert module_validator() == True
