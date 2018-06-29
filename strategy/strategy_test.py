import unittest

from strategy import LongWalkHomeStrategy, ShortWalkHomeStrategy
from penguin import Penguin


class StrategyTest(unittest.TestCase):

    def test_strategy_pattern(self):
        Penguin(LongWalkHomeStrategy()).walk_home()
        Penguin(ShortWalkHomeStrategy()).walk_home()


if __name__ == '__main__':
    unittest.main()