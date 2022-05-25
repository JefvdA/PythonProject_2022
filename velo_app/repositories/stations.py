import random

from classes.bike import Bike


class Stations():
    def __init__(self):
        self.stations = []

    def add_station(self, station):
        self.stations.append(station)

    def get_stations(self):
        return self.stations
    
    def add_bike(self):
        index = random.randint(0, len(self.stations) - 1)
        self.stations[index].put_bike_in_slot(Bike())