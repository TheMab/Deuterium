import time

class Switcher(object):
    # active = bool
    # last_frame_id = str
    # last_switch_time = int(time.time())

    def __init__(self):
        self.active = False
        self.last_frame_id = 'a'

    def switch_frame(self, new_frame_id):

        print ""
        print "old:  " + str(self.last_frame_id)
        print "new:  " + str(new_frame_id)
        print ""


        if new_frame_id == self.last_frame_id:
            pass
        else:
                self.last_frame_id = new_frame_id
                self.last_switch_time = int(time.time())
                self.active = False
                print "SWITCHER DISABLED!!!!!!!!!!!!!:"
                print "switcher is: "+ str(self.active)



    # def switch_frame(self, new_frame_id):
    #     curr_time = time.gmtime
    #
    #     if curr_time - self.last_switch_time > 3:
    #         self.active = True
    #         self.switch(new_frame_id)
    #     else:
    #         print "switch attempt less than 3 seconds from last"


    def is_active(self):
        curr_time = int(time.time())
        print "switcher is: (is_active before) "+ str(self.active)

        print "current: "+ str(curr_time)
        print "last: "+ str(self.last_switch_time)

        if (curr_time - self.last_switch_time) > 3:
            self.active = True
            print "switcher enabled"
        else:
            pass

        print "switcher is: "+ str(self.active)

        return self.active

