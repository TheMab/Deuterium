import os, re, cv2


def get_fileList(dir):
	rootDir = './'+dir
	for dirName, subdirList, fileList in os.walk(rootDir):
		return fileList

def clean_dir(my_list):
	r = re.compile(".*.pyc|.*__init__.py")
	new_list = filter(r.match, my_list)
	unmatched = list(set(my_list) - set(new_list))
	return unmatched


def populate_list(my_list, dir_list):

	for f in dir_list:
		my_list.append((f,f))
	return my_list

# def enumerate_cameras():
# 	""" Returns a list of cameras detected """
# 	cam_index = []
#
# 	for i in range(0,2):
# 		camera = cv2.VideoCapture(i)
# 		_, img = camera.read()
# 		if _:
# 			cam_index.append(i)
#         camera.release()
# 	return cam_index

