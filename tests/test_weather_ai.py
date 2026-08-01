from modules.weather_ai.weather_ai import weather_ai


def test_weather_ai():

    assert weather_ai() == True
