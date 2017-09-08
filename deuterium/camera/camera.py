import cv2

from deuterium import deuterium


class VideoCamera(object):


    def __init__(self, first_path, second_path, switcher, detection):

        if first_path.isdigit():
            first_path = int(first_path)

        if second_path.isdigit():
            second_path = int(second_path)


        self.video_one = cv2.VideoCapture(first_path)
        self.video_two = cv2.VideoCapture(second_path)
        self.switcher = switcher
        self.detection = detection


    def get_frame(self):
        _, image_one = self.video_one.read()
        __, image_two = self.video_two.read()
        switcher = self.switcher
        detection = self.detection

        try:
            image_final = deuterium(image_one, image_two, switcher, detection)
        except:
            image_final = switcher.get_last_active(image_one, image_two)
            print "Ball Not Found"


        ret, jpeg = cv2.imencode('.jpg',image_final)
        return jpeg.tobytes()


