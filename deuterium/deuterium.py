# -*- coding: utf-8 -*-
"""Main module."""

# import necessary packages
from flask import Flask, render_template, Response, request, session, jsonify
from flask_bootstrap import Bootstrap
from forms import pathToVideo
from camera.camera import  Camera
from camera.newCamera import VideoCamera
from switcher.Switcher import Switcher
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


@app.route('/video_feed')
def video_feed():
    print "initialising switcher"
    radius_switcher = Switcher()
    camera = VideoCamera(session['firstPath'],session['secondPath'], radius_switcher)

    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed/a')
def video_feed_a():
    camera_a = VideoCamera(first_path=session['firstPath'], second_path=None, switcher=None)

    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera_a),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed/b')
def video_feed_b():
    camera_b = VideoCamera(first_path=None,second_path=session['secondPath'], switcher=None)

    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera_b),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/result', methods=['POST'])
def result():
    form = pathToVideo()

    session['firstPath'] = form.firstPath.data
    session['secondPath'] = form.secondPath.data
    session['radius_a'] = 0
    session['radius_b'] = 0

    return render_template('result.html')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)


