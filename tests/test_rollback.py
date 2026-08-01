from modules.rollback.rollback import rollback


def test_rollback():

    assert rollback() == True
