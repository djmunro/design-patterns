from abc import abstractmethod

from beverage import Beverage


class AddonDecorator(Beverage):

    @abstractmethod
    def cost(self):
        """Gets the cost of the beverage"""
        return
