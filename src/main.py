from managers.api_manager import ApiManager

def run():
    print('hier alles doen kiddo\'s')

def test_GetStations():
    # api = ApiManager()
    # res = api.getAllStations()
    succes, res = ApiManager.getAllStations()
    print(succes)
    # print(res[200:205])
    print("###################################")
    for station in res:
        if station['namen']['lang'] == "Utrecht Centraal":
            print(station)
        # print(station['namen']['lang'])

def test_getDeparturesForStation():
    succes, res = ApiManager.getDeparturesForStation()
    print(succes)
    print(res)

test_GetStations()
test_getDeparturesForStation()