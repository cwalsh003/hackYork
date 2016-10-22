import requests
import jsonify
import pprint
import redis
# from collections import OrderedDict
myDict = dict()
myDict2 = dict()
ctr = 0
r = requests.get("http://api.spotcrime.com/crimes.json?lat=39.962914&lon=-76.75632000000002&radius=0.2&key=.")
myDict = r.json()
myDict2[1] = {}
myDict2[1]["rating"] = 1

rdb = redis.StrictRedis(host='localhost', port=6379, db=0, password='foobared')


for crimes in myDict["crimes"]:
    # print(crimes.keys())
    ctr = ctr + 1
    myDict2[ctr] = {}
    myDict2[ctr]["rating"] = 1

    for majorKey in crimes.keys():
        if (majorKey == "type" or majorKey == "lat" or majorKey == "lon" or majorKey == "date"):
            if(majorKey == "lat"):
                myDict2[ctr]["lat"] = crimes[majorKey]
            if(majorKey == "lon"):
                myDict2[ctr]["lon"] = crimes[majorKey]
            if(majorKey == "date"):
                myDict2[ctr]["date"] = crimes[majorKey]

            else:
                if(crimes[majorKey] == "Arrest"):
                    myDict2[ctr]["rating"] = myDict2[ctr]["rating"] + 5 % 100
                elif(crimes[majorKey] == "Arson"):
                    myDict2[ctr]["rating"] = myDict2[ctr]["rating"] + 5 % 100
                elif(crimes[majorKey] == "Assault"):
                    myDict2[ctr]["rating"] = myDict2[ctr]["rating"] + 5 % 100
                elif(crimes[majorKey] == "Burglary"):
                     myDict2[ctr]["rating"] = myDict2[ctr]["rating"] + 5 % 100
                elif(crimes[majorKey] == "Robbery"):
                    myDict2[ctr]["rating"] = myDict2[ctr]["rating"] + 5 % 100
                elif(crimes[majorKey] == "Shooting"):
                    myDict2[ctr]["rating"] = myDict2[ctr]["rating"] + 5 % 100
                elif(crimes[majorKey] == "Theft"):
                    myDict2[ctr]["rating"] = myDict2[ctr]["rating"] + 5 % 100
                elif(crimes[majorKey] == "Vandalism"):
                    myDict2[ctr]["rating"] = myDict2[ctr]["rating"] + 5 % 100
                elif(crimes[majorKey] == "Other"):
                    myDict2[ctr]["rating"] = myDict2[ctr]["rating"] + 5 % 100
        rdb.append(ctr, myDict2)

value = r.get('foo')
print(value)

            # print(majorKey)
