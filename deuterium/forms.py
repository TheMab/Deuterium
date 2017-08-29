from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField

class pathToVideo(FlaskForm):
	firstPath = StringField('path to first video')
	secondPath = StringField('path to second video')
	# firstFile = FileField
	submit = SubmitField('Submit') 
