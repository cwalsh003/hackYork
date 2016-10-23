import json
from flask import request, Flask, jsonify


app = Flask(__name__)

@app.route('/rating',methods=['GET','POST'])

def callDevice():
    location = request.args
    print(request.args)

    crimedata = request.json
    print(crimedata)
    print(json.dumps(crimedata['crimes']))
    payload = {
        "geolocation": {
            "lat" : location['lat'],
            "lon" : location['lon'],
            "time": location['time']
        }
    }
    return jsonify(rating=4)
    #return jsonify(rating = bossPlaya.finalRating(location['lat'],location['lon']))
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)
