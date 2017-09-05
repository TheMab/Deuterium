# -*- coding: utf-8 -*-
"""Main module."""

# import necessary packages
from flask import Flask, render_template, Response, request, session
from flask_bootstrap import Bootstrap
from forms import pathToVideo
from camera.camera import VideoCamera
from switcher.switch_algorithm.radius_switcher import RadiusSwitcher
from switcher.switch_algorithm.interval_switcher import IntervalSwitcher

import os, time

app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET','POST'])
def index():
    form = pathToVideo()

    return render_template('index.html', form=form)


def gen(camera):

    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def get_selected_switcher(file, threshold):
    if file == 'radius_switcher.py':
        return RadiusSwitcher(threshold)
    elif file == 'interval_switcher.py':
        return IntervalSwitcher(threshold)
    else:
        print "Default switcher initialised"
        return RadiusSwitcher(3)



@app.route('/video_feed')
def video_feed():

    # Initialising switcher
    switcher = get_selected_switcher(session['switcherSelect'], session['switcherThreshold'] )

    camera = VideoCamera(session['firstPath'],session['secondPath'], switcher)

    # """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route('/result', methods=['POST'])
def result():
    form = pathToVideo()
    session['firstPath'] = form.firstPathSelect.data
    session['secondPath'] = form.secondPathSelect.data
    session['switcherSelect'] = form.switcherSelect.data
    session['switcherThreshold'] = request.form['threshold']

    return render_template('result.html')





if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)


