from modules.module_validator.module_validator import module_validator


def command(args):

    if len(args) < 2:
        print("❌ Anna moduulin nimi")
        return False

    module_name = args[1]

    return module_validator([module_name])