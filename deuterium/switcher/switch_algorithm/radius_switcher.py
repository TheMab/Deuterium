import time, imutils
from switcher.Switcher import Switcher

class RadiusSwitcher(Switcher):

    # class variables
    frame_a_id = 'a'
    frame_b_id = 'b'
    frame_a = object
    frame_b = object

    # returns current enabled state of switcher
    def is_active(self):


        curr_time = time.time()
        time_since_last_switch = curr_time - self.last_switch_time

        # If threshold time has surpassed since last switch, re-enable switcher
        if time_since_last_switch > int(self.threshold):
            self.activate()

        return self.active



    def switch_logic(self, frame_a, frame_b):

        try:
            # unpack frame tuple
            frame_a, radius_a = frame_a
            frame_b, radius_b = frame_b
            # set class variable, used get_last_frame() method
            self.frame_a = frame_a
            self.frame_b = frame_b

        except:
            "something went wrong with frame tuple in radius switcher"

        # switching logic
        if radius_a>radius_b:
            if self.last_frame_id == self.frame_a_id:
                return frame_a
            # checks if threshold time has passed and enables switcher accordingly
            elif self.is_active():
                self.switch_frame(self.frame_a_id)
                self.deactivate()
                return frame_a
            else:
                # in the case that previous frame is different and switcher is not enabled
                return frame_b
        else:
            if self.last_frame_id == self.frame_b_id:
                return frame_b
            elif self.is_active():
                self.switch_frame(self.frame_b_id)
                self.deactivate()
                return frame_b
            else:
                return frame_a

    # returns self.last_
    def get_last_active(self, frame_a, frame_b):
        if self.last_frame_id == self.frame_a_id:
            return imutils.resize(frame_a, width=900)
        else:
            return imutils.resize(frame_b, width=900)

