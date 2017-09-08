import imutils


def deuterium(frame_a, frame_b, switcher, detector):


    frame_a_tuple = detector.detection_algo(frame_a)
    frame_b_tuple = detector.detection_algo(frame_b)

    # f, r = frame_a_tuple
    # xf, xr = frame_b_tuple

    try:
        frame_final = switcher.switch_logic(frame_a_tuple, frame_b_tuple)
        switcher.last_active = frame_final
    except:
        # frame_final = switcher.get_last_active(f, xf)
        print "blah"

    # if _ or __ :
    #     pass
    # else:
    #     "checkboard"
    #     frame_final = imutils.resize('calibration/checkboard/G0124222.JPG', width= 900 )

    frame_final = imutils.resize(frame_final, width=900)
    return frame_final
