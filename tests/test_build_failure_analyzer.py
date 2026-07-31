from modules.build_failure_analyzer.build_failure_analyzer import build_failure_analyzer


def test_build_failure_analyzer():

    assert build_failure_analyzer() == True
