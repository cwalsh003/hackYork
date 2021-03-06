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


# pass location[lat],location[lon] through function
def finalRating(lat, lon, jsonData):
    lat = str(round(float(lat), 2))
    lon = str(round(float(lon), 2))



    myDict = json.dumps(jsonData)
    rating = 0
    latSum = 0
    lonSum = 0

    keyArr = []
    majorKeys = []

    rdb = redis.StrictRedis(host='54.174.126.53', port=6379, db=0)

    for crimes in myDict["crimes"]:
        for majorKey in crimes.keys():
            majorKeys.append(majorKey)


        print(crimes)
        print(majorKey)
        if (majorKey == "lat" or majorKey == "lon"):
            if (majorKey == "lat"):
                latSum += crimes[majorKey]
                ctr = ctr + 1
            if (majorKey == "lon"):
                lonSum += crimes[majorKey]
                ctr = ctr + 1

    keyArr.append(latSum / ctr)
    keyArr.append(lonSum / ctr)

    keyTuple = tuple(keyArr)

    myDict2[keyTuple] = {}
    myDict2[keyTuple]['rating'] = 0

    for keys in myDict2.keys():
        for majorKey in majorKeys:
            if (crimes[majorKey] == "Arrest"):
                rating += 5
            elif (crimes[majorKey] == "Arson"):
                rating += 8
            elif (crimes[majorKey] == "Assault"):
                rating += 5
            elif (crimes[majorKey] == "Burglary"):
                rating += 4
            elif (crimes[majorKey] == "Robbery"):
                rating += 2
            elif (crimes[majorKey] == "Shooting"):
                rating += 7
            elif (crimes[majorKey] == "Theft"):
                rating += 4
            elif (crimes[majorKey] == "Vandalism"):
                rating += 3
            elif (crimes[majorKey] == "Other"):
                rating += 2

    myDict2[keyTuple]["rating"] = rating

    rdb.append(keys, myDict2)

    return rating
