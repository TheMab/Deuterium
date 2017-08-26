# -*- coding: utf-8 -*-
"""Main module."""

# import necessary packages
from flask import Flask, render_template, Response, request, session, jsonify
from flask_bootstrap import Bootstrap
from forms import pathToVideo
from camera.camera import  Camera
import os

app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET','POST'])
def index():
    form = pathToVideo()

    # session['firstPath'] = "/resources/RightCam.mp4"


    return render_template('index.html', form=form)


def gen(camera):
    # Camera.setPath('/Users/mabs/Desktop/deuterium/deuterium/resources/RightCam.mp4')
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():

    Camera.setPath(session['firstPath'])

    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/result', methods=['POST'])
def result():
    form = pathToVideo()

    session['firstPath'] = form.firstPath.data
    session['secondPath'] = form.secondPath.data
    return render_template('result.html')

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)


