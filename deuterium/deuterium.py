# -*- coding: utf-8 -*-
"""Main module."""

# import necessary packages
from flask import Flask, render_template, Response, request, session
from flask_bootstrap import Bootstrap
from forms import pathToVideo
from camera.camera import VideoCamera
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

    # Initialising switcher
    print "initialising switcher"
    radius_switcher = Switcher()

    camera = VideoCamera(session['firstPath'],session['secondPath'], radius_switcher)

    # """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route('/result', methods=['POST'])
def result():
    form = pathToVideo()

    session['firstPath'] = form.firstPathSelect.data
    session['secondPath'] = form.secondPathSelect.data

    return render_template('result.html')





if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)


