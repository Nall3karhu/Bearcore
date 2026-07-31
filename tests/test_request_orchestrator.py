from modules.request_orchestrator.request_orchestrator import request_orchestrator


def test_request_orchestrator():

    assert request_orchestrator() == True
