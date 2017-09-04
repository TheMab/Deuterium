import imutils
from detection.detection_algorithms.toolbox import colour_detection


def ball_detection(frame_a, frame_b, switcher):
    frame_a_tuple = colour_detection(frame_a)
    frame_b_tuple = colour_detection(frame_b)
    radius_switcher = switcher

    try:
        frame_final = radius_switcher.switch_logic(frame_a_tuple, frame_b_tuple)
        radius_switcher.last_active = frame_final
    except:
        frame_final = radius_switcher.get_last_active()

    frame_final = imutils.resize(frame_final, width=900)
    return frame_final
