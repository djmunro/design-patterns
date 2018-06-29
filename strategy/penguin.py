class Penguin(object):

    def __init__(self, strategy):
        self.strategy = strategy

    def walk_home(self):
        self.strategy.walk_home()
