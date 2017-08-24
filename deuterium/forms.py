from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class pathToVideo(FlaskForm):
	firstPath = StringField('path to first video')
	secondPath = StringField('path to second video')
	submit = SubmitField('Submit') 
