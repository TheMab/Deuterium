# import necessary packages
import time
import imutils

# switcher class
class Switcher(object):

    # shows if switcher is enabled or not
    active = bool
    # user specified threshold
    threshold = int
    # stores the id for the last frame yielded
    last_frame_id = str
    # stores time last switch took place
    last_switch_time = int(time.time())

    # switcher requires self and threshold parameters when being initialised
    def __init__(self, threshold):
        # default set as enabled to allow first allocation of last_frame_id
        self.active = True
        self.threshold = threshold

    # method should be called after the frame has been switched. ie. last_frame_id != new_frame_id
    # resets last switch time
    def switch_frame(self, new_frame_id):
        self.last_switch_time = int(time.time())
        self.last_frame_id = new_frame_id

    # to deactivate switcher
    def deactivate(self):
        print "deactivated at  "+ str(int(time.time()))
        self.active = False

    # to activate switcher
    def activate(self):
        self.active = True

    # returns if switcher is active or not, should be overridden in subclass for a more specific function
    def is_active(self):
        return self.active

    # the actual switching logic that defines the type of switcher, MUST be implemented by subclass
    def switch_logic(self):
        '''To be implemented by subclass'''
        pass

    # input parameter: instance of switcher and the two frames in the same order as passed in other methods
    # should return frame last used as per defined id in the subclass
    def get_last_active(self, frame_a, frame_b):
        '''To be implemented by subclass'''
        pass