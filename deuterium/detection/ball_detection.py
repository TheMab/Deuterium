from toolbox import colour_detection, delete_background
import imutils, time
from flask import session
from switcher.Switcher import Switcher


def get_final_frame(a, b, switcher):

    frame_a, radius_a = a
    frame_b, radius_b = b
    radius_switcher = switcher

    if radius_a>radius_b:
        return frame_a
    else:
        return frame_b

def ball_detection(frame_a, frame_b, switcher):
    frame_a_tuple = colour_detection(frame_a)
    frame_b_tuple = colour_detection(frame_b)
    radius_switcher = switcher

    frame_final = get_final_frame(frame_a_tuple, frame_b_tuple, radius_switcher)
    frame_final = imutils.resize(frame_final, width=600)

    return frame_final
