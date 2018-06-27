import unittest

from observer.iobserverable import IObserverable
from observer.phone_display import PhoneDisplay
from observer.weather_station import WeatherStation


class ObserverTests(unittest.TestCase):

    def setUp(self):
        self.weather_station = WeatherStation()
        self.phone_display = PhoneDisplay(self.weather_station)
        self.weather_station.add(self.phone_display)

    def test_observerable_is_type_observerable(self):
        assert isinstance(self.weather_station, IObserverable)

    def test_wheather_station_can_update(self):
        self.weather_station.notify()


if __name__ == '__main__':
    unittest.main()