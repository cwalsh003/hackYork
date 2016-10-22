import requests
import jsonify
import json
import pprint
import redis
from flask import Flask, request
# from collections import OrderedDict
myDict = dict()
myDict2 = dict()
ctr = 0



r = requests.get("http://api.spotcrime.com/crimes.json?lat=39.962914&lon=-76.75632000000002&radius=0.2&key=.")
myDict = r.json()

latSum = 0
lonSum = 0

keyArr = []
majorKeys = []

rdb = redis.StrictRedis(host='54.174.126.53', port=6379, db=0)


for crimes in myDict["crimes"]:
    for majorKey in crimes.keys():
        majorKeys.append(majorKey)
        print(crimes )
        print( majorKey)
        if ( majorKey == "lat" or majorKey == "lon"):
            if(majorKey == "lat"):
                latSum += crimes[majorKey]
                ctr = ctr + 1
            if(majorKey == "lon"):
                lonSum += crimes[majorKey]
                ctr = ctr + 1

keyArr.append(latSum / ctr)
keyArr.append(lonSum / ctr)

keyTuple = tuple(keyArr)

myDict2[keyTuple] = {}
myDict2[keyTuple]['rating'] = 0

for keys in myDict2.keys():
    for majorKey in majorKeys:
        print(keys)

        if(crimes[majorKey] == "Arrest"):
            myDict2[keys]["rating"] = (myDict2[keys]["rating"] + 5) % 100
        elif(crimes[majorKey] == "Arson"):
            myDict2[keys]["rating"] = (myDict2[keys]["rating"] + 5) % 100
        elif(crimes[majorKey] == "Assault"):
            myDict2[keys]["rating"] = (myDict2[keys]["rating"] + 5) % 100
        elif(crimes[majorKey] == "Burglary"):
             myDict2[keys]["rating"] = (myDict2[keys]["rating"] + 5) % 100
        elif(crimes[majorKey] == "Robbery"):
            myDict2[keys]["rating"] = (myDict2[keys]["rating"] + 5) % 100
        elif(crimes[majorKey] == "Shooting"):
            myDict2[keys]["rating"] = (myDict2[keys]["rating"] + 5) % 100
        elif(crimes[majorKey] == "Theft"):
            myDict2[keys]["rating"] = (myDict2[keys]["rating"] + 5) % 100
        elif(crimes[majorKey] == "Vandalism"):
            myDict2[keys]["rating"] = (myDict2[keys]["rating"] + 5) % 100
        elif(crimes[majorKey] == "Other"):
            myDict2[keys]["rating"] = (myDict2[keys]["rating"] + 5) % 100
            rdb.append(keys, myDict2)




            # print(majorKey)
