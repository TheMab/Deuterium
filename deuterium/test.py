import cv2

def enumerate_cameras():
	""" Number of cameras detected """
	cam_index = []

	for i in range(0,2):
		camera = cv2.VideoCapture(i)
		_, img = camera.read()
		if _:
			cam_index.append(i)
			camera.release()
	return cam_index


print enumerate_cameras()