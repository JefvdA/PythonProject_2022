import json
import pickle

from constants import VELO_JSON, VELO_PICKLE
from classes.station import Station
from repositories.stations import Stations
from repositories.users import Users


class VeloApp:
    def __init__(self) -> None:
        self.stations = Stations() # Initialize the stations object
        self.users = Users() # Initialize the users object

    def initialize(self):
        with open(VELO_JSON) as json_file: # Open the geojson file - Get the stations from the file
            data = json.load(json_file)
            for station in data["features"]:
                streetName = station["properties"]["Straatnaam"]
                slots = station["properties"]["Aantal_plaatsen"]

                station = Station(streetName, slots)
                self.stations.add_station(station)

        [self.stations.add_bike() for i in range(4200)] # Add bikes to the stations

        self.users.generate_users(55000) # Generate users

    def load_data(self):
        with open(VELO_PICKLE, "rb") as f:
            self = pickle.load(f)

    def save_data(self):
        with open(VELO_PICKLE, "wb") as f:
            pickle.dump(self, f)

    
    # GETTERS SETTERS
    def get_stations(self):
        return self.stations
    
    def get_users(self):
        return self.users