import cv2
from flask import session
from detection.ball_detection import ball_detection


class VideoCamera(object):


    def __init__(self, first_path, second_path, switcher):

        if first_path.isdigit():
            first_path = int(first_path)

        if second_path.isdigit():
            second_path = int(second_path)


        self.video_one = cv2.VideoCapture(first_path)
        self.video_two = cv2.VideoCapture(second_path)
        self.switcher = switcher



    def get_frame(self):
        _, image_one = self.video_one.read()
        __, image_two = self.video_two.read()
        switcher = self.switcher

        try:
            image_final = ball_detection(image_one, image_two, switcher)
        except:
            image_final = image_one
            print "Ball Not Found"

        ret, jpeg = cv2.imencode('.jpg',image_final)
        return jpeg.tobytes()


