from datetime import datetime

from pathlib import Path

import shutil



BASE_DIR = Path(__file__).resolve().parent.parent.parent


BACKUP_DIR = BASE_DIR / "backups"



def create_backup():

    BACKUP_DIR.mkdir(
        exist_ok=True
    )


    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    backup_path = BACKUP_DIR / (
        f"BearCore_backup_{timestamp}"
    )


    shutil.copytree(

        BASE_DIR,

        backup_path,

        ignore=shutil.ignore_patterns(

            "__pycache__",

            ".pytest_cache",

            "*.pyc"

        )

    )


    return {

        "success":
            True,

        "time":
            datetime.now().isoformat(),

        "backup":
            str(backup_path)

    }



def backup_status():

    return {

        "module":
            "backup_manager",

        "status":
            "ready"

    }