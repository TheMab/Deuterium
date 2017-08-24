import cv2
import imutils
import numpy as np



fgbg = cv2.createBackgroundSubtractorMOG2()

def delete_background(frame):
    fgmask = fgbg.apply(frame)
    res = cv2.bitwise_and(frame, frame, mask = fgmask)
    return res

def add_framenumber(frame, number):

    newFrame = cv2.rectangle(frame, (5, 14), (200, 50), (210, 210, 210), -1)
    newFrame = cv2.putText(frame, 'Frame number: ' + str(number), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    number+=1
    return newFrame , number


def colour_detection(frame):

    greenLower = (29, 86, 6)
    greenUpper = (64, 255, 255)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        cv2.putText(frame, 'Ball Radius: ' + str(round(radius, 3)), (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 0, 255), 1)

        # only proceed if the radius meets a minimum size
        if radius > 2:
            # print radius
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)

        newFrame = frame
        return newFrame