import os
import shutil
from datetime import datetime


BACKUP_FOLDER = ".backups"


def backup_manager(args=None):

    print("🐻 Backup Manager käynnissä")

    source = "modules"


    if not os.path.exists(source):

        print(
            "❌ Backup-kohdetta ei löydy"
        )

        return False


    os.makedirs(
        BACKUP_FOLDER,
        exist_ok=True
    )


    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )


    backup_path = os.path.join(
        BACKUP_FOLDER,
        timestamp
    )


    try:

        shutil.copytree(
            source,
            backup_path
        )


        print(
            "✅ Backup luotu:"
        )

        print(
            backup_path
        )


        return backup_path


    except Exception as e:

        print(
            "❌ Backup virhe:"
        )

        print(e)

        return False