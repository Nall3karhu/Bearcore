from modules.backup_manager.backup_manager import backup_manager


def test_backup_manager():

    assert backup_manager() == True
