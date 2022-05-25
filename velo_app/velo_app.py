import json
import pickle

from classes.station import Station
from repositories.stations import Stations
from repositories.users import Users

VELO_JSON = "assets/velo.geojson"
VELO_PICKLE = "assets/velo.pickle"


class VeloApp:
    def initialize(self):
        self.stations = Stations() # Initialize the stations object
        self.users = Users() # Initialize the users object

        with open(VELO_JSON) as json_file: # Open the geojson file - Get the stations from the file
            data = json.load(json_file)
            for station in data["features"]:
                streetName = station["properties"]["Straatnaam"]
                slots = station["properties"]["Aantal_plaatsen"]

                station = Station(streetName, slots)
                self.stations.add_station(station)

        [self.stations.add_bike() for i in range(4200)] # Add bikes to the stations

        self.users.generate_users(55000) # Generate users

        print(self.users)

    def save_data(self):
        with open(VELO_PICKLE, "wb") as f:
            pickle.dump(self, f)