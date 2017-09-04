import time

class Switcher(object):
    active = bool
    last_frame_id = str
    last_switch_time = int(time.time())

    def __init__(self):
        self.active = True

    def switch_frame(self, new_frame_id):
        self.last_switch_time = int(time.time())
        self.last_frame_id = new_frame_id

    def deactivate(self):
        print "deactivated at  "+ str(int(time.time()))
        self.active = False

    def activate(self):
        self.active = True

    def is_active(self):
        return self.active

    def switch_logic(self):
        '''To be implemented by subclass'''
        pass