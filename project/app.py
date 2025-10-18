import serial
import csv
import pickle
import time
import json
import numpy as np
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Thread

# Initialize Flask and SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Connect to Arduino 
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=2)

# Loading pre-trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

CSV_FILE = 'sensor_data_log.csv'
HEADER = [
    'Timestamp', 'TempDS18B20', 'Humidity', 'TempDHT11',
    'pH', 'Turbidity', 'EC', 'DO', 'Predicted_Class'
]

# Ensure CSV header exists
with open(CSV_FILE, 'a', newline='') as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(HEADER)


def read_serial_loop():
    """Continuously reads incoming data from Arduino and streams updates"""
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if not line:
                continue

            # Parse key:value pairs (e.g., TempDS18B20:25.6,pH:7.1,...)
            segments = line.split(',')
            data = {}
            for seg in segments:
                key, val = seg.split(':')
                data[key.strip()] = float(val.strip())

            # Create feature vector for ML model (order must match training)
            features = [
                data['TempDS18B20'], data['Humidity'], data['TempDHT11'],
                data['pH'], data['Turbidity'], data['EC'], data['DO']
            ]

            # Optional preprocessing
            arr = np.array(features).reshape(1, -1)
            prediction = model.predict(arr)[0]

            data_out = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "TempDS18B20": data['TempDS18B20'],
                "Humidity": data['Humidity'],
                "TempDHT11": data['TempDHT11'],
                "pH": data['pH'],
                "Turbidity": data['Turbidity'],
                "EC": data['EC'],
                "DO": data['DO'],
                "Prediction": str(prediction)
            }

            # Log to CSV
            with open(CSV_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(list(data_out.values()))

            # Emit to web clients
            socketio.emit('update', data_out)

            time.sleep(1)

        except Exception as e:
            print(f"Error processing data: {e}")
            continue


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Run Arduino listener in background thread
    thread = Thread(target=read_serial_loop)
    thread.daemon = True
    thread.start()

    # Start Flask-SocketIO server
    socketio.run(app, host='0.0.0.0', port=5000)
