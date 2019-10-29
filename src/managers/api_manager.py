import http.client, urllib.request, urllib.parse, urllib.error, base64
from typing import Dict
import json

class ApiManager(object):

    clientUrl = 'gateway.apiportal.ns.nl'
    baseUrl = '/public-reisinformatie/api/v2/'
    depUrl = 'departures[?dateTime][&maxJourneys][&lang][&station][&uicCode][&source]'
    headers = {
        # Request headers
        # David Demmers personal secondary key
        'Ocp-Apim-Subscription-Key': '6c0387de772249b7bed9164ee423d2af',
    }

    def getAllStations() -> [bool,dict]:
        params = urllib.parse.urlencode({

        })
        try:
            conn = http.client.HTTPSConnection(ApiManager.clientUrl)
            conn.request("GET", ApiManager.baseUrl + "stations?%s" % params, "{body}", ApiManager.headers)
            response = conn.getresponse()
            data = response.read().decode('utf-8')
            conn.close()
            return True, json.loads(data)['payload']
        except Exception as e:
            print(f"Err: {e}")
            return False, set()

    def getDeparturesForStation() -> [bool,dict]:
        params = urllib.parse.urlencode({
            # Request parameters
            'dateTime': '{string}',
            'maxJourneys': '25',
            'lang': 'nl',
            'station': '{string}',
            'uicCode': '{string}',
            'source': '{string}',
        })
        try:
            conn = http.client.HTTPSConnection(ApiManager.clientUrl)
            conn.request("GET", ApiManager.baseUrl + "departures?%s" % params, "{body}", ApiManager.headers)
            response = conn.getresponse()
            data = response.read().decode('utf-8')
            conn.close()
            return True, json.loads(data)
        except Exception as e:
            print(f"Err: {e}")
            return False, set()