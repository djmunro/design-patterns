from observer.iobserverable import IObserverable


class WeatherStation(IObserverable):

    def __init__(self):
        self.observers = []

    def add(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        pass

    def notify(self):
        for observer in self.observers:
            observer.update()

    def temperature(self):
        return 72