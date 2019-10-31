import http.client, urllib.request, urllib.parse, urllib.error, base64
from typing import Dict
import json

class ApiManager(object):

    # Base http client where we are connecting to
    clientUrl = 'gateway.apiportal.ns.nl'
    # basis api url
    baseUrl = '/public-reisinformatie/api/v2/'
    # Http request headers
    headers = {
        # David Demmers personal secondary key
        'Ocp-Apim-Subscription-Key': '6c0387de772249b7bed9164ee423d2af',
    }
    # dict to put the stations in after a initial pull to speedup the rest of the program
    stationList:dict = None
    def getAllStations() -> [bool,dict]:
        """
        Make a get request and get all the stations.
        Return a succes and a dict of the payload data
        """
        params = urllib.parse.urlencode({

        })
        if ApiManager.stationList == None:
            try:
                conn = http.client.HTTPSConnection(ApiManager.clientUrl)
                conn.request("GET", ApiManager.baseUrl + "stations?%s" % params, "{body}", ApiManager.headers)
                response = conn.getresponse()
                data = response.read().decode('utf-8')
                conn.close()
                ApiManager.stationList = json.loads(data)['payload']
                return True, ApiManager.stationList
            except Exception as e:
                print(f"Err: {e}")
                return False, set()
        else:
            print('get stations from memory')
            return True, ApiManager.stationList

    def getDeparturesForStation(stationCode:str) -> [bool,dict]:
        """
        Make a get request and get all the departurs from a specific station from it\'s stationCode
        Return a succes and a dict of the payload data
        """
        params = urllib.parse.urlencode({
            # Request parameters
            'maxJourneys': '25',
            'lang': 'nl',
            'station': stationCode
        })
        try:
            conn = http.client.HTTPSConnection(ApiManager.clientUrl)
            conn.request("GET", ApiManager.baseUrl + "departures?%s" % params, "{body}", ApiManager.headers)
            response = conn.getresponse()
            data = response.read().decode('utf-8')
            conn.close()
            return True, json.loads(data)['payload']['departures']
        except Exception as e:
            print(f"Err: {e}")
            return False, set()