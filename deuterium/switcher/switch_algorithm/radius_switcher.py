from switcher import switcher
import time

class RadiusSwitcher(switcher.Switcher):



    def is_active(self):

        curr_time = time.time()
        time_since_last_switch = curr_time - self.last_switch_time

        if time_since_last_switch > 3:
            self.activate()

        return self.active



    def switch_logic(self, frame_a, frame_b):

        frame_a_id = 'a'
        frame_b_id = 'b'

        try:
            frame_a, radius_a = frame_a
            frame_b, radius_b = frame_b
        except:
            "something went wrong with frame tuple in radius switcher"

        if radius_a>radius_b:
            if self.last_frame_id == frame_a_id:
                # self.last_active = frame_a
                return frame_a
            elif self.is_active():
                self.switch_frame(frame_a_id)
                self.deactivate()
                # self.last_active = frame_a
                return frame_a
            else:
                # self.last_active = frame_b
                return frame_b
        else:
            if self.last_frame_id == frame_b_id:
                # self.last_active = frame_b
                return frame_b
            elif self.is_active():
                self.switch_frame(frame_b_id)
                self.deactivate()
                # self.last_active = frame_b
                return frame_b
            else:
                # self.last_active = frame_a
                return frame_a


    def get_last_active(self):
        return self.last_active