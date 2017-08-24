from flask import Flask, render_template, Response
from flask_bootstrap import Bootstrap
# emulated camera
from camera import camera

# If you are using a webcam -> no need for changes
# if you are using the Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera.Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)