from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route('/rating')

def callDevice(deviceID):
    location = request.args

    device = devices.get(deviceID)

    payload = {
        "geolocation": {
            "lat" : location['lat'],
            "lon" : location['lon'],
            "time": location['time']
        }

    }

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)
