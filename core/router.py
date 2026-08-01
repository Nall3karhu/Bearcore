from core.module_manager import run_module


SYSTEM_COMMANDS = {
    "create": "developer",
    "reload": "developer",
    "status": "developer",
    "analyze": "developer",
    "build": "developer",
    "test": "developer",
    "fix": "developer",
}


def route(command):

    parts = command.strip().split()

    if not parts:
        return False

    first = parts[0].lower()

    if first in SYSTEM_COMMANDS:

        module = SYSTEM_COMMANDS[first]

        new_command = module + " " + command

        return run_module(new_command)

    return run_module(command)