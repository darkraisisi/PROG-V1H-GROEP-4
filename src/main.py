from managers.api_manager import ApiManager
from classes.front_page import frontPage

def run():
    frontPage.__init__()
    # test_GetStations()
    # test_getDeparturesForStation('UT')

def test_GetStations():
    # run the getAllStations from the apiManager class
    # catch the 2 returned value's: a succes and the result
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

run()