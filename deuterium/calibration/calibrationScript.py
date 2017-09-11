import numpy as np
import cv2
import glob

"""This script runs calibration using OpenCV standard calibration methods. Uses a 9x7 sized chessboard"""

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('/media/sf_Shared_Folder/Sandbox/Chessboard V3/*.png')

counter = 0

chessboardWidth = 9
chessboardHeight = 7

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardHeight*chessboardWidth,3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardWidth,0:chessboardHeight].T.reshape(-1,2)

imageSize = 0
imgHeight = 0
imgWidth = 0

for fname in images:
    print(fname)
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    imageSize = gray.shape[::-1]
    imgHeight, imgWidth = img.shape[:2]

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (chessboardWidth,chessboardHeight),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (chessboardWidth,chessboardHeight), corners2,ret)
        filenameStr = "/media/sf_Shared_Folder/Sandbox/Chessboard V3/ChessboardOverlay/" + str(counter) + ".png"
        print(filenameStr)
        cv2.imwrite(filenameStr,img)
        counter += 1
        cv2.waitKey(500)


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, imageSize, None, None)


newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(imgWidth, imgHeight),1,(imgWidth, imgHeight))

counter2 = 0
for fname in images:
    img = cv2.imread(fname)
    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    # crop the image
    x, y, w, h = roi
    dst = dst[y:y + h, x:x + w]
    filenameStr2 = "/media/sf_Shared_Folder/Sandbox/Chessboard V3/undistorted/" + str(counter2) + ".png"
    cv2.imwrite(filenameStr2, dst)
    counter2 += 1


img = cv2.imread("/media/sf_Shared_Folder/Sandbox/Chessboard V3/img/vlcsnap-2017-09-09-21h12m11s616.png")
imgUndistort = cv2.undistort(img, mtx, dist, None, newcameramtx)
cv2.imwrite("/media/sf_Shared_Folder/Sandbox/Chessboard V3/img/undistorted.png", imgUndistort)

mean_error = 0
tot_error = 0

for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    tot_error += error

print("total error: ", mean_error/len(objpoints))

cv2.destroyAllWindows()