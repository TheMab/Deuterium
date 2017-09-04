# Import the os module, for the os.walk function
import os
#
# # Set the directory you want to start from
# rootDir = './resources'
# for dirName, subdirList, fileList in os.walk(rootDir):
#     print fileList


# Set the directory you want to start from
rootDir = './resources'
(dirName, subdirList, fileList) = os.walk(rootDir)
print fileList