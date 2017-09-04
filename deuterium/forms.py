from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, SelectField
import os

class pathToVideo(FlaskForm):
	# firstPath = StringField('path to first video')
	# secondPath = StringField('path to second video')
	# firstFile = FileField
	submit = SubmitField('Submit')

	dir = os.path.dirname(__file__)

	fileOptionList = [(0,0),(1,1)]
	rootDir = './resources'
	for dirName, subdirList, fileList in os.walk(rootDir):
		for f in fileList:
			fileOptionList.append((dir+'/resources/'+f,f))

	firstPathSelect = SelectField(u'First Path: ', choices=fileOptionList)
	secondPathSelect = SelectField(u'Second Path: ', choices=fileOptionList)


