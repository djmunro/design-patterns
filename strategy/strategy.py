import abc


class Strategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def walk_home(self):
        pass


class LongWalkHomeStrategy(Strategy):

    def walk_home(self):
        print('1 mile south, then 2 miles under the water, then 500 feet on the left')


class ShortWalkHomeStrategy(Strategy):

    def walk_home(self):
        print('1 block up on the left, next to the iceberg')
