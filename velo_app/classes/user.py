from typing import List

from classes.bike import Bike


class User:
    index = 0

    def __init__(self, first_name, last_name) -> None:
        self.id = User.index
        self.first_name = first_name
        self.last_name = last_name
        self.bikes = []
        self.MAX_BIKES = 1
        User.index += 1

    # GETTERS / SETTERS
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_bikes(self) -> List[Bike]:
        return self.bikes

    def get_bike_amount(self) -> int:
        return len(self.bikes)
    
    def get_max_bikes(self) -> int:
        return self.MAX_BIKES

    def take_bike(self, station) -> bool:
        if self.get_bike_amount() < self.get_max_bikes():
            bike = station.take_bike_from_slot()
            if bike is not None:
                self.bikes.append(bike)
                return True
            return False

        return False
    
    def put_bike_away(self, station) -> bool:
        if self.get_bike_amount() > 0:
            return station.put_bike_in_slot(self.bikes.pop())

        return False

    def __str__(self) -> str:
        return f'{self.id} : {self.first_name} {self.last_name} : bikes: {self.get_bike_amount()}'