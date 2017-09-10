# -*- coding: utf-8 -*-
"""Main module."""

import os

# import necessary packages
from flask import Flask, render_template, Response, request, session
from flask_bootstrap import Bootstrap

from camera.camera import VideoCamera
from controllers.run_controller import get_selected_detector, get_selected_switcher, gen
from forms import pathToVideo

# initialise app
app = Flask(__name__)
# flask-bootstrap
Bootstrap(app)
# secret key required for wtform encryption
app.secret_key = os.urandom(24)


# Route for the homepage, renders index template
@app.route('/', methods=['GET','POST'])
def index():
    form = pathToVideo()

    return render_template('index.html', form=form)



@app.route('/video_feed')
def video_feed():

    # Initialising switcher using user selection of switcher
    switcher = get_selected_switcher(session['switcherSelect'], session['switcherThreshold'] )
    detection = get_selected_detector(session['detectionSelect'])

    # Initialising emulated openCV camera using video path selected by user
    camera = VideoCamera(session['firstPath'],session['secondPath'], switcher, detection)

    # """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



# Route to results page after submitting form on index page
@app.route('/result', methods=['POST'])
def result():
    # declare form from form.py
    form = pathToVideo()

    # user option selections from form saved as sessions to be accessible via different routes
    session['firstPath'] = form.firstPathSelect.data
    session['secondPath'] = form.secondPathSelect.data
    session['switcherSelect'] = form.switcherSelect.data
    session['switcherThreshold'] = request.form['threshold']
    session['detectionSelect'] = form.detectionSelect.data

    return render_template('result.html')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)


