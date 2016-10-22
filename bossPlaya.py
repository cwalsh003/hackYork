import requests
import json
import pprint
import redis
import mechanicalsoup
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

# from collections import OrderedDict
myDict = dict()
myDict2 = dict()
ctr = 0
#pass location[lat],location[lon] through function
def finalRating(lat,lon):

    br = browser = mechanicalsoup.Browser()

    # Broser options
    br.set_handle_equiv( True )
    #br.set_handle_gzip( True )
    br.set_handle_redirect( True )
    br.set_handle_referer( True )
    br.set_handle_robots( False )

    br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )
    br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]

    lat1 = str(round(float(lat),2))
    lon1 = str(round(float(lon),2))
    print(lat1 + '\n')
    print(lon1 + '\n')
    url = ("http://api.spotcrime.com/crimes.json?lat=" + lat1 + "&lon=" + lon1 + "&radius=0.2&key=.")
    print(url)
    br.open(url)
    thepage = browser.get(url)
    print(thepage)
    soup = BeautifulSoup(thepage, "html.parser")
    for crimes in soup.findAll('pre'):
        myDict = json.loads(crimes)
        print(json.dumps(myDict))

    latSum = 0
    lonSum = 0

    keyArr = []
    majorKeys = []

    rdb = redis.StrictRedis(host='54.174.126.53', port=6379, db=0)


    for crimes in myDict["crimes"]:
            for majorKey in crimes.keys():
                    majorKeys.append(majorKey)
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
                rating += 5
            elif(crimes[majorKey] == "Arson"):
                rating += 8
            elif(crimes[majorKey] == "Assault"):
                rating += 5
            elif(crimes[majorKey] == "Burglary"):
                rating += 4
            elif(crimes[majorKey] == "Robbery"):
                rating += 2
            elif(crimes[majorKey] == "Shooting"):
                rating += 7
            elif(crimes[majorKey] == "Theft"):
                rating += 4
            elif(crimes[majorKey] == "Vandalism"):
                rating += 3
            elif(crimes[majorKey] == "Other"):
                rating += 2

    myDict2[keyTuple]["rating"]=rating
    rdb.append(keys, myDict2)
    return rating
