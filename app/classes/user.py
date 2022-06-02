from typing import List

from tools.logger.logger import Logger

from classes.bike import Bike


class User:
    index = 0

    def __init__(self, first_name, last_name) -> None:
        self.id = User.index
        self.first_name = first_name
        self.last_name = last_name
        self.bikes = []
        self.MAX_BIKES = 1
        self.logger = Logger()
        User.index += 1

    # GETTERS / SETTERS
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_bikes(self) -> List[Bike]:
        return self.bikes

    def get_bike_count(self) -> int:
        return len(self.bikes)
    
    def get_max_bikes(self) -> int:
        return self.MAX_BIKES

    def take_bike(self, station, amount = 1) -> bool:
        i = 0
        while i < amount and self.get_bike_count() < self.get_max_bikes():
            bike: Bike = station.take_bike_from_slot(self)
            if bike is not None:
                self.bikes.append(bike)
                i += 1
                self.logger.add_log(f'{self.get_name()} took a bike {bike.get_id()} from {station.get_name()}')
            elif i > 0:
                return True
            else:
                return False
        if i > 0:
            return True
        else:
            return False

    
    def put_bike_away(self, station, amount = 1) -> bool:
        i = 0
        while i < amount and self.get_bike_count() > 0:
            bike: Bike = self.bikes.pop()
            succes = station.put_bike_in_slot(bike, self)
            if succes:
                i += 1
                self.logger.add_log(f'{self.get_name()} put a bike {bike.get_id()} away at {station.get_name()}')
            elif i > 0:
                return True
            else:
                return False
        if i > 0:
            return True
        else:
            return False
        

    def __str__(self) -> str:
        return f'{self.id} : {self.first_name} {self.last_name} : bikes: {self.get_bike_count()}'