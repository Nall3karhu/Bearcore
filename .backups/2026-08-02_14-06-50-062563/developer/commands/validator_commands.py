from modules.module_validator.module_validator import module_validator


def validate(args=None):

    if args is None:
        args = []

    if not args:

        print("❌ Anna moduulin nimi")

        return False

    return module_validator(args)