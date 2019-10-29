from managers.api_manager import ApiManager
# import display_trains
def run():
    print('hier alles doen kiddo\'s')

def test_GetStations():
    succes, res = ApiManager.getAllStations()
    print(succes)
    if succes:
        for station in res:
            if station['land'] == "NL":
                # print(station)
                print(f"Code: {station['code']}, {station['namen']['lang']} ")

def test_getDeparturesForStation(stationCode:str):
    succes, res = ApiManager.getDeparturesForStation(stationCode)
    if succes:
        for departure in res:
            print(f"Vertrektijd: {departure['actualDateTime']}, Eindstation: {departure['direction']}, Spoor: {departure['plannedTrack']}, Trein Type: {departure['product']['longCategoryName']}")

test_GetStations()
test_getDeparturesForStation('UT')