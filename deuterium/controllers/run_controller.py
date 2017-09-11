from switcher.switch_algorithm.radius_switcher import RadiusSwitcher
from switcher.switch_algorithm.interval_switcher import IntervalSwitcher
from detection.detection_algorithms.colour_detection import Colour_detector
from detection.detection_algorithms.background_subtraction import Background_substractor



def get_selected_switcher(file, threshold):
    """inputs file name of switcher and threshold setting for that switcher
    returns the iniatlised switcher variable according to user selection """
    if file == 'radius_switcher.py':
        return RadiusSwitcher(threshold)
    elif file == 'interval_switcher.py':
        return IntervalSwitcher(threshold)
    #
    #elif():
    #Custom routes to be added here
    #
    #

    else:
        # Default switcher is radius switcher with 3 second lock out period
        print "Default switcher initialised"
        return RadiusSwitcher(3)



def get_selected_detector(detector):
    """ detemins which detector was selected by user"""
    if detector == 'colour_detection.py':
        return Colour_detector()
    elif detector == 'background_subtraction.py':
        return Background_substractor()
    #
    #elif():
    #Custom routes to be added here
    #
    #
    else:
        # Default detection is colour_detection
        print "Default switcher initialised"
        return Colour_detector()



def gen(camera):
    """ generate camera used for streaming streaming of video to browser"""

    # infinite loop to keep iterating until camera has no other frames
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')