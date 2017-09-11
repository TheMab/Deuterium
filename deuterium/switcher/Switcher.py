# import necessary packages
import time
import imutils

# switcher class
class Switcher(object):
    """ Switcher class, switch_logic and get_last_active methods must be implemented by subclass"""


    # shows if switcher is enabled or not
    active = bool
    # user specified threshold
    threshold = int
    # stores the id for the last frame yielded
    last_frame_id = str
    # stores time last switch took place
    last_switch_time = int(time.time())


    def __init__(self, threshold):
        """switcher requires self and threshold parameters when being initialised"""
        # default set as enabled to allow first allocation of last_frame_id
        self.active = True
        self.threshold = threshold


    def switch_frame(self, new_frame_id):
        """method should be called after the frame has been switched. ie. last_frame_id != new_frame_id
        resets last switch time"""
        self.last_switch_time = int(time.time())
        self.last_frame_id = new_frame_id

    def deactivate(self):
        """to deactivate switcher"""
        print "deactivated at  "+ str(int(time.time()))
        self.active = False

    def activate(self):
        """to activate switcher"""
        self.active = True

    def is_active(self):
        """ returns if switcher is active or not, should be overridden in subclass for a more specific function"""
        return self.active

    def switch_logic(self):
        """the actual switching logic that defines the type of switcher, MUST be implemented by subclass.
        To be implemented by subclass"""
        pass


    def get_last_active(self, frame_a, frame_b):
        """input parameter: instance of switcher and the two frames in the same order as passed in other methods
        should return frame last used as per defined id in the subclass
        To be implemented by subclass"""
        pass