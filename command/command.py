from abc import ABCMeta, abstractmethod


class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        """Executes the command"""
        return

    @abstractmethod
    def unexecute(self):
        """Undo's the execution of the last command"""
        return


class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def unexecute(self):
        self.light.off()


class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def unexecute(self):
        self.light.on()
