import cv2
from base_camera import BaseCamera
import imutils
import os
from flask import session

class Camera(BaseCamera):


    pathToVideo = 0

    @staticmethod
    def setPath(source):
            Camera.pathToVideo= source



    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.pathToVideo)

        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            img = imutils.resize(img, 600)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()

