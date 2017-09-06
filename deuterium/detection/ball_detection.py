import imutils
# from detection.detection_algorithms.toolbox import colour_detection


def ball_detection(frame_a, frame_b, switcher, detection):
    frame_a_tuple = detection.detection_algo(frame_a)
    frame_b_tuple = detection.detection_algo(frame_b)

    try:
        frame_final_a = switcher.switch_logic(frame_a_tuple, frame_b_tuple)
        switcher.last_active = frame_final_a
    except:
        print "except triggered in ball detection"

    frame_final_a = imutils.resize(frame_final_a, width=900)
    return frame_final_a
