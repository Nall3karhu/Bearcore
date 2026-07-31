from modules.health_monitor.health_monitor import health_monitor


def test_health_monitor():

    assert health_monitor() == True
