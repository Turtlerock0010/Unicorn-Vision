import io
import time
from flask import Flask, Response
from picamera2 import Picamera2

app = Flask(__name__)

# Initialize Picamera2
picam2 = Picamera2()
# Use a standard 720p or 480p configuration
config = picam2.create_video_configuration(main={"size": (848, 480), "format": "RGB888"})
picam2.configure(config)
picam2.start()

def generate_frames():
    while True:
        # Create an in-memory byte stream
        stream = io.BytesIO()
        # Capture a single frame into the stream
        picam2.capture_file(stream, format='jpeg')
        
        frame = stream.getvalue()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
        # Small sleep to prevent CPU Max-out (adjust for desired FPS)
        time.sleep(0.03) 

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return "<h1>PiCam2 Live Stream</h1><img src='/video_feed' width='100%'>"

if __name__ == '__main__':
    # Listen on all network interfaces at port 5000
    app.run(host='0.0.0.0', port=8080, threaded=True)
