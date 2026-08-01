from modules.developer.scan import scan_project
from modules.developer.analyze import analyze_project
from modules.developer.checker import check_code
from modules.developer.suggest import suggest_fixes
from modules.developer.fix import auto_fix
from modules.developer.tester import run_tests
from modules.developer.history import show_history
from modules.developer.knowledge import module_info
from modules.developer.inspector import inspect_module
from modules.developer.brain import show_brain
from modules.developer.goals import show_goals
from modules.developer.dependencies import analyze_dependencies



def command(args):

    cmd = args[0]


    if cmd == "scan":
        scan_project()
        return True


    if cmd == "analyze":
        analyze_project()
        return True


    if cmd == "check":
        check_code()
        return True


    if cmd == "suggest":
        suggest_fixes()
        return True


    if cmd == "fix":
        auto_fix()
        return True


    if cmd == "test":
        run_tests()
        return True


    if cmd == "history":
        show_history()
        return True


    if cmd == "brain":
        show_brain()
        return True


    if cmd == "goals":
        show_goals()
        return True


    if cmd == "dependencies":
        analyze_dependencies()
        return True


    if cmd == "info":
        module_info(args[1:])
        return True


    if cmd == "inspect":
        inspect_module(args[1:])
        return True


    return False