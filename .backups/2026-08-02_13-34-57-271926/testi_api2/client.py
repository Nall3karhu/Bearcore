import requests


def get(url):

    response = requests.get(url, timeout=10)

    return response.json()