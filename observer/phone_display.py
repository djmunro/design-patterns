from observer.iobserver import IObserver


class PhoneDisplay(IObserver):

    def __init__(self, weather_station):
        self.weather_station = weather_station

    def update(self):
        temperature = self.weather_station.temperature()
        print("the temperature is now {}".format(temperature))