from detection.Detector import Detector
import cv2

class Colour_detector(Detector):
    """class containing detection algorithm for colour based detection of a green ball"""

    def detection_algo(self, frame):
        """ detection algorithm for this subclass, returns processed image and radius of the ball"""
        greenLower = (29, 86, 6)
        greenUpper = (64, 255, 255)

        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        mask = cv2.Canny(mask, 100, 200)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            # only proceed if the radius is present
            if radius:
                # draw the circle on the frame,
                cv2.circle(frame, (int(x), int(y)), int(radius),
                           (0, 255, 255), 2)

            return frame, radius