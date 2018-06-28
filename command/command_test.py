import unittest

from command import LightOnCommand, LightOffCommand
from reciever import LightReciever
from invoker import RemoteInvoker


class CommandTests(unittest.TestCase):

    def test_command_pattern(self):
        light = LightReciever()
        remote = RemoteInvoker(LightOnCommand(light), LightOffCommand(light))
        remote.press_on()


if __name__ == '__main__':
    unittest.main()
