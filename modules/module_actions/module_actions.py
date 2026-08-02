from modules.analyzer.analyzer import analyzer
from modules.module_tester.module_tester import module_tester
from modules.module_backup.module_backup import module_backup
from modules.module_repair.module_repair import module_repair



def run_action(
    action,
    module_name
):

    if action == "analyze":

        return analyzer(
            module_name
        )


    if action == "test":

        return module_tester(
            module_name
        )


    if action == "backup":

        return module_backup(
            module_name
        )


    if action == "repair":

        return module_repair(
            module_name
        )


    return {

        "success": False,

        "message": "Tuntematon toiminto"

    }