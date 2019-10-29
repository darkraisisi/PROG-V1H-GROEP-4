import http.client
import json
import urllib.parse


headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'c7779d626b66498a808b7568aed7ef9c',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/public-reisinformatie/api/v2/stations?%s" % params, "{body}", headers)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    payloadObject = data['payload']
    stationDict = {}
    stationList = []
    for station in payloadObject:
        stationDict[station['namen']['lang']] = station['code']
        stationList.append(station['namen']['lang'])

    print(stationDict)
    print(stationList)


    conn.close()
except Exception as e:
    print("Fout: {} {}".format(e.errno, e.strerror))