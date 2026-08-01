MODULE_INFO = {}


def register(name, info):
    MODULE_INFO[name] = info


def get(name):
    return MODULE_INFO.get(name)


def all_modules():
    return MODULE_INFO