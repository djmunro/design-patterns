from addon_decorator import AddonDecorator


class Caramel(AddonDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 2


class AlternativeCaramel(AddonDecorator):

    def cost(self):
        return 2


class AlternativeWhip(AddonDecorator):

    def cost(self):
        return 1.50
