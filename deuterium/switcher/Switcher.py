import time

class Switcher(object):
    # active = bool
    # last_frame_id = str
    # last_switch_time = int(time.time())

    def __init__(self):
        self.active = False
        self.last_frame_id = 'a'

    def switch_frame(self, new_frame_id):
        pass

