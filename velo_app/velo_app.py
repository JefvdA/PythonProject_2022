import json
import pickle

from classes.station import Station
from repositories.stations import Stations

VELO_JSON = "assets/velo.geojson"
VELO_PICKLE = "assets/velo.pickle"


class VeloApp:
    def initialize(self):
        stations = Stations() # Initialize the stations object

        with open(VELO_JSON) as json_file: # Open the geojson file - Get the stations from the file
            data = json.load(json_file)
            for station in data["features"]:
                streetName = station["properties"]["Straatnaam"]
                slots = station["properties"]["Aantal_plaatsen"]

                station = Station(streetName, slots)
                stations.add_station(station)

        [stations.add_bike() for i in range(4200)] # Add bikes to the stations

        print(stations) # Print the stations

    def save_data(self):
        with open(VELO_PICKLE, "wb") as f:
            pickle.dump(self, f)