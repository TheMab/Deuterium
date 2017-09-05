# Import the os module, for the os.walk function
import os, re
#
# # Set the directory you want to start from
# rootDir = './resources'
# for dirName, subdirList, fileList in os.walk(rootDir):
#     print fileList


# Set the directory you want to start from
def get_fileList(dir):
	rootDir = './'+dir
	for dirName, subdirList, fileList in os.walk(rootDir):
		return fileList



def clean_dir(my_list):
    r = re.compile(".*.pyc|.*__init__.py")
    new_list = filter(r.match, my_list)
    unmatched = list(set(my_list) - set(new_list))
    return unmatched

print clean_dir(get_fileList('switcher/switch_algorithm'))
