import shutil
from pathlib import Path
from datetime import datetime

BACKUP_FOLDER = ".backups"


def backup_manager(args=None):

    print("🐻 Backup Manager käynnissä")

    project_root = Path(__file__).resolve().parents[2]

    source = project_root / "modules"
    backup_root = project_root / BACKUP_FOLDER

    if not source.exists():
        print("❌ Backup-kohdetta ei löydy")
        return False

    backup_root.mkdir(exist_ok=True)

    while True:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S-%f"
        )

        backup_path = backup_root / timestamp

        if not backup_path.exists():
            break

    try:

        shutil.copytree(
            source,
            backup_path
        )

        print("✅ Backup luotu:")
        print(backup_path)

        return True

    except Exception as e:

        print("❌ Backup virhe:")
        print(e)

        return False