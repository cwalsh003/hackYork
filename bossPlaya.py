import requests
import json
import pprint
# from collections import OrderedDict
myDict = dict()

r = requests.get('http://api.spotcrime.com/crimes.json?lat=39.962914&lon=-76.75632000000002&radius=0.2&key=.')
myDict = r.json()

# print(r.headers['content-type'])
# print(json.loads(r.text))
# print(json.dumps(r.text))


for crimes in myDict['crimes']:
    print(crimes)
    # for crimes in myDict['crimes'][keys]:
    #     print(crimes + '\n')
