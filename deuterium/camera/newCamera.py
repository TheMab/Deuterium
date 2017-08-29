# camera.py

import cv2
import imutils
from flask import session
from detection.ball_detection import ball_detection
from detection.toolbox import colour_detection

class VideoCamera(object):


    def __init__(self, first_path, second_path, switcher):
        if switcher:
            self.video_one = cv2.VideoCapture(first_path)
            self.video_two = cv2.VideoCapture(second_path)
            self.switcher = switcher
        elif first_path:
            self.video_one = cv2.VideoCapture(first_path)
            self.video_two = None
            self.switcher = None

        elif second_path:
            self.video_two = cv2.VideoCapture(second_path)
            self.video_one = None
            self.switcher = None


    def get_frame(self):
        if self.video_one and self.video_two:
            print (3)
            _, image_one = self.video_one.read()
            __, image_two = self.video_two.read()
            switcher = self.switcher

            image_final = ball_detection(image_one, image_two, switcher)
            ret, jpeg = cv2.imencode('.jpg',image_final)
            return jpeg.tobytes()

        elif(self.video_one == None):
            print (2)
            __, image_two = self.video_two.read()
            image_two = imutils.resize(image_two, 300)
            ret, jpeg = cv2.imencode('.jpg', image_two)
            return jpeg.tobytes()

        elif(self.video_two == None):
            print (1)

            __, image_one = self.video_one.read()
            image_one = imutils.resize(image_one, 300)
            ret, jpeg = cv2.imencode('.jpg', image_one)
            return jpeg.tobytes()
