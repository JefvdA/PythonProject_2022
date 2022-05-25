from classes.slot import Slot


class Station:
    index = 0

    def __init__(self, streetName, slots):
        Station.index += 1
        self.id = Station.index
        self.steetName = streetName
        self.availableSlots = slots
        self.slots = self.generate_slots(slots)

    def generate_slots(self, x):
        slots = []
        for i in range(x):
            slots.append(Slot(str(self.id) + "-" + str(i), None))
        return slots

    def get_total_slots(self):
        return len(self.slots)

    def get_available_slots(self):
        return self.availableSlots

    def put_bike_in_slot(self, bike):
        if self.availableSlots <= 0:
            return False # Fail - no slots available
        
        # find next available slot with 'availableSlots' - put bike in slot - decrease availableSlots
        index = len(self.slots) - self.availableSlots
        self.slots[index].bike = bike
        self.availableSlots -= 1
        
        return True # Succes - slot has been added

    def __str__(self) -> str:
        return "Station " + str(self.id) + ": " + self.steetName + " (" + str(len(self.slots) - self.availableSlots) + " / " + str(len(self.slots)) + " slots taken)"