from modules.request_connector.request_connector import request_connector


def test_request_connector():

    assert request_connector() == True
