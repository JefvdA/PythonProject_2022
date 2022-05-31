from tools.logger.logger import Logger

from classes.bike import Bike
from classes.slot import Slot
from classes.user import User


class Station:
    index = 0

    def __init__(self, streetName, slots):
        self.id = Station.index
        self.steetName = streetName
        self.availableSlots = slots
        self.slots = self.generate_slots(slots)
        self.logger = Logger()
        Station.index += 1

    def generate_slots(self, x) -> list[Slot]:
        slots = []
        for i in range(x):
            slots.append(Slot(str(self.id) + "-" + str(i), None))
        return slots

    def get_name(self) -> str:
        return f'{self.id} : {self.steetName}'

    def get_total_slots(self) -> int:
        return len(self.slots)

    def get_available_slots(self) -> int:
        return self.availableSlots

    def get_bike_count(self) -> int:
        return self.get_total_slots() - self.get_available_slots()

    def put_bike_in_slot(self, bike: Bike, user: User) -> bool:
        if self.availableSlots <= 0:
            return False # Fail - no slots available
        
        # Find next available slot with 'availableSlots' - put bike in slot - decrease availableSlots
        index = len(self.slots) - self.availableSlots
        self.slots[index].leave_bike(bike)
        self.availableSlots -= 1
        
        if user is not None:
            self.logger.add_log(f'{user.get_name()} put a bike {bike.get_id()} away at {self.get_name()}')
        return True # Succes - slot has been added

    def take_bike_from_slot(self, user: User) -> Bike:
        if self.availableSlots >= self.get_total_slots():
            return None # Fail - no bikes available

        # Find last slot with bike - take bike from slot - increase availableSlots
        index = len(self.slots) - self.availableSlots - 1
        bike = self.slots[index].take_bike()
        self.availableSlots += 1

        self.logger.add_log(f'{user.get_name()} took a bike {bike.get_id()} from {self.get_name()}')
        return bike # Succes - bike has been taken, return it

    def __str__(self) -> str:
        return "Station " + str(self.id) + ": " + self.steetName + " (" + str(len(self.slots) - self.availableSlots) + " / " + str(len(self.slots)) + " slots taken)"