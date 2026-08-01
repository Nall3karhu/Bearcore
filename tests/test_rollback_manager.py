from modules.rollback_manager.rollback_manager import rollback_manager


def test_rollback_manager():

    assert rollback_manager() == True
