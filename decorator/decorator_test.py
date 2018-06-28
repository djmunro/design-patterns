import unittest

from coffee import Espresso, AlternativeEspresso
from addons import Caramel, AlternativeCaramel, AlternativeWhip


class DecoratorTests(unittest.TestCase):

    def test_decorator_pattern(self):
        specialty_drink = Caramel(Espresso())
        self.assertEquals(3, specialty_drink.cost())

    def test_more_suitable_approach(self):
        addons = [AlternativeCaramel(), AlternativeWhip()]
        specialty_drink = AlternativeEspresso(addons)
        self.assertEquals(4.50, specialty_drink.cost())


if __name__ == '__main__':
    unittest.main()
