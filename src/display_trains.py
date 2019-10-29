import http.client
import json
import urllib.parse

key = {'Ocp-Apim-Subscription-Key': 'c7779d626b66498a808b7568aed7ef9c'}

params = urllib.parse.urlencode({
    'maxJourneys': '25',
    'station': 'Ut'#hier variabele gebruiken voor wijzigen station
})

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/public-reisinformatie/api/v2/departures?" + params, headers=key)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    payloadObject = data['payload']
    departuresList = payloadObject['departures']

    for departure in departuresList:
        print('Vertrektijd: {}, Eindstation: {}, Spoor: {}, Trein Type: {}'.format(departure['actualDateTime'], departure['direction'], departure['plannedTrack'], departure['product']['longCategoryName']))

    conn.close()
except Exception as e:
    print("Fout: {} {}".format(e.errno, e.strerror))