from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
import os, re


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



class pathToVideo(FlaskForm):

	fileDirList = clean_dir(get_fileList('resources'))
	switcherDirList = clean_dir(get_fileList('switcher/switch_algorithm'))
	detectionDirList = clean_dir(get_fileList('detection/detection_algorithms'))

	switcherOptionList = populate_list([],switcherDirList)
	detectionOptionList =populate_list([],detectionDirList)

	dir = os.path.dirname(__file__)
	fileOptionList = [(0, 0), (1, 1)]
	for f in fileDirList:
		fileOptionList.append((dir+'/resources/'+f,f))


	firstPathSelect = SelectField(u'First Path: ', choices=fileOptionList)
	secondPathSelect = SelectField(u'Second Path: ', choices=fileOptionList)
	detectionSelect = SelectField(u'Select Detection: ', choices=detectionOptionList)
	switcherSelect = SelectField(u'Select Switcher: ', choices=switcherOptionList)
	submit = SubmitField('Submit')