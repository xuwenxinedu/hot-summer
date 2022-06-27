import cv2
import numpy as np
import time
from flask import Flask, render_template, Response
from flask_cors import CORS

vc = cv2.VideoCapture(0)
vc.set(3, 640)
vc.set(4, 480)
time.sleep(0.5)

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def index():
    # video streaming 的主界面
    return render_template('index.html')

def gen():
    while True:
        ret, frame = vc.read()
        img = cv2.imencode(".jpg", frame)[1].tobytes()
        yield(b"--frame\r\n"
             b"Content-Type: images/jpeg\r\n\r\n" + img + b"\r\n")
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")

def gen_api():
    ret, frame = vc.read()
    img = cv2.imencode(".jpg", frame)[1].tobytes()
    return img

@app.route('/video_feed_api')
def video_feed_api():
    # while True:
        return Response(gen_api())
    
app.run(host="0.0.0.0", port=8087, threaded=True)

