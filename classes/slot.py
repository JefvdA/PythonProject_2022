from classes.bike import Bike


class Slot:
    def __init__(self, id: int, bike: Bike):
        self.id = id
        self.bike = bike

    def take_bike(self) -> Bike:
        bike = self.bike
        self.bike = None

        return bike

    def leave_bike(self, bike: Bike) -> None:
        self.bike = bike