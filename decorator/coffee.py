from beverage import Beverage


class Espresso(Beverage):

    def cost(self):
        return 1


class AlternativeEspresso(Beverage):

    def __init__(self, addons):
        self.addons = addons

    def cost(self):
        coffee_cost = 1
        total = coffee_cost
        for addon in self.addons:
            total += addon.cost()
        return total
