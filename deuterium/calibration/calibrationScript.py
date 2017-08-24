import numpy as np
import cv2
import os
import glob

from os import path

objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

dir = os.path.dirname(__file__)
pathToCheckerboardImages = dir + '/checkboard/Image3.tif'

print(pathToCheckerboardImages)

# You are going to have a for loop that loops through
# every image
# e.g. images = glob.glob('/checkerboard/')

testMat = cv2.imread(pathToCheckerboardImages)
cv2.imshow("test", testMat)

gray = cv2.cvtColor(testMat,cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(gray, (12, 12), None)

img = cv2.drawChessboardCorners(gray, (12, 12), corners, ret)

cv2.imshow("Corners", img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    exit()
