import imutils


def deuterium(frame_a, frame_b, switcher, detector):
    """ Script for main deuterium logic, frames processed with detection and switching algorithm, final frame
    returned to camera for streaming """

    frame_a_tuple = detector.detection_algo(frame_a)
    frame_b_tuple = detector.detection_algo(frame_b)

    try:
        frame_final = switcher.switch_logic(frame_a_tuple, frame_b_tuple)
        switcher.last_active = frame_final
    except:
        print "Foo"


    frame_final = imutils.resize(frame_final, width=900)
    return frame_final
