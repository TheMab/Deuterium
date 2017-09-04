import imutils

from detection.detection_algorithms.toolbox import colour_detection


def get_final_frame(a, b, switcher):

    radius_b = 0
    radius_a = 0

    try:
        frame_a, radius_a = a
        frame_b, radius_b = b
        radius_switcher = switcher
    except:
        "something went wrong"


    if radius_a>radius_b:
        return frame_a
    else:
        return frame_b



def ball_detection(frame_a, frame_b, switcher):
    frame_a_tuple = colour_detection(frame_a)
    frame_b_tuple = colour_detection(frame_b)
    radius_switcher = switcher

    frame_final = get_final_frame(frame_a_tuple, frame_b_tuple, radius_switcher)
    frame_final = imutils.resize(frame_final, width=900)

    return frame_final
