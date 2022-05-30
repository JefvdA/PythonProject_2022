import random
from typing import List

from classes.bike import Bike
from classes.station import Station


class Stations:
    def __init__(self) -> None:
        self.stations = []

    def add_station(self, station):
        self.stations.append(station)

    def get_stations(self) -> List[Station]:
        return self.stations
    
    def add_bike(self):        
        bike_is_added = False
        while not bike_is_added:
            index = random.randint(0, len(self.stations) - 1)

            bike_is_added = self.stations[index].put_bike_in_slot(Bike(), None)

    def __str__(self) -> str:
        string = ""
        for station in self.stations:
            string += str(station) + "\n"
        return string