import numpy as np
import cv2
import os
import glob
import imutils

from os import path

objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

dir = os.path.dirname(__file__)
pathToCheckerboardImages = dir + '/checkboard/*.JPG'

print(pathToCheckerboardImages)

# You are going to have a for loop that loops through
# every image
images = glob.glob(pathToCheckerboardImages)

for fname in images:


    testMat = imutils.resize(cv2.imread(fname), 600)

    cv2.imshow("test", testMat)

    gray = cv2.cvtColor(testMat,cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (7, 9), None)

    img = cv2.drawChessboardCorners(gray, (7, 9), corners, ret)

    cv2.imshow("Corners", img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        exit()
