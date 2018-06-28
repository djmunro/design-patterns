from abc import ABCMeta, abstractmethod


class Beverage(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def cost(self):
        """Gets the cost of the beverage"""
        return
