# -*- coding: utf-8 -*-
"""Main module."""

# import necessary packages
from flask import Flask, render_template, Response, request, session
from flask_bootstrap import Bootstrap
from forms import pathToVideo
from camera.camera import VideoCamera
from switcher.switch_algorithm.radius_switcher import RadiusSwitcher
from switcher.switch_algorithm.interval_switcher import IntervalSwitcher
from detection.detection_algorithms.colour_detection import Colour_detector
from detection.detection_algorithms.background_subtraction import Background_substractor
import os, time


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

# generate camera used for streaming streaming of video to browser
def gen(camera):

    # infinite loop to keep iterating until camera has no other frames
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# inputs file name of switcher and threshold setting for that switcher
# returns the iniatlised switcher variable according to user selection
def get_selected_switcher(file, threshold):
    if file == 'radius_switcher.py':
        return RadiusSwitcher(threshold)
    elif file == 'interval_switcher.py':
        return IntervalSwitcher(threshold)
    else:
        # Default switcher is radius switcher with 3 second lock out period
        print "Default switcher initialised"
        return RadiusSwitcher(3)


# Route for streaming MJPEG video file
def get_selected_detector(detector):
    if detector == 'colour_detection.py':
        return Colour_detector()
    elif detector == 'background_subtraction.py':
        return Background_substractor()
    else:
        # Default detection is colour_detection
        print "Default switcher initialised"
        return Colour_detector()

@app.route('/video_feed')
def video_feed():

    # Initialising switcher using user selection of switcher
    switcher = get_selected_switcher(session['switcherSelect'], session['switcherThreshold'] )
    detection = get_selected_detector(session['detectionSelect'])

    # Inisitalising emulated openCV camera using video path selected by user
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


