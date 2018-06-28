class RemoteInvoker(object):

    def __init__(self, on, off):
        self.on = on
        self.off = off

    def press_on(self):
        self.on.execute()

    def press_off(self):
        self.off.execute()
