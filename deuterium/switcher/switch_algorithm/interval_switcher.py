import time
import imutils
from switcher.Switcher import Switcher

class IntervalSwitcher(Switcher):
    """ class for Interval switcher, switches feed every x seconds defined by threshold"""
    frame_a_id = 'a'
    frame_b_id = 'b'
    frame_a = object
    frame_b = object


    def switch_logic(self, frame_a, frame_b):
        """ switching logic defined by this subclass"""
        curr_time = int(time.time())
        threshold = int(self.threshold)
        print "curr time: " + str(int(curr_time))

        try:
            frame_a, radius_a = frame_a
            frame_b, radius_b = frame_b
            self.frame_a = frame_a
            self.frame_b = frame_b
        except:
            print "something went wrong with frame tuple in interval switcher"

        print (curr_time % (threshold*2))

        if curr_time % (threshold*2) > (threshold-1):
            self.last_frame_id = self.frame_a_id
            return frame_a
        else:
            self.last_frame_id = self.frame_b_id
            return frame_b


    def get_last_active(self, frame_a, frame_b):
        """ returns the last frame that was used in case no ball was detected, for continuity of stream """
        if self.last_frame_id == self.frame_a_id:
            return imutils.resize(frame_a, width=900)
        else:
            return imutils.resize(frame_b, width=900)



