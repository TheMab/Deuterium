from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, SelectField, IntegerField, validators
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


class pathToVideo(FlaskForm):

	dir = os.path.dirname(__file__)


	fileOptionList = [(0,0),(1,1)]
	switcherOptionList = []

	fileDirList = clean_dir(get_fileList('resources'))
	switcherDirList = clean_dir(get_fileList('switcher/switch_algorithm'))

	for f in fileDirList:
		fileOptionList.append((dir+'/resources/'+f,f))

	for f in switcherDirList:
		switcherOptionList.append((f,f))

	firstPathSelect = SelectField(u'First Path: ', choices=fileOptionList)
	secondPathSelect = SelectField(u'Second Path: ', choices=fileOptionList)

	switcherSelect = SelectField(u'Select Switcher: ', choices=switcherOptionList)
	submit = SubmitField('Submit')

