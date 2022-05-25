from classes.slot import Slot


class Station:
    index = 0

    def __init__(self, streetName, slots):
        Station.index += 1
        self.id = Station.index
        self.steetName = streetName
        self.slots = self.generate_slots(slots)

    def generate_slots(self, x):
        slots = []
        for i in range(x):
            slots.append(Slot(str(self.id) + "-" + str(i), None))
        return slots

    def get_slot_amount(self):
        return len(self.slots)

    def put_bike_in_slot(self, bike):
        for slot in self.slots:
            if slot.bike is None:
                slot.bike = bike
                return True
        return False

    def __str__(self):
        return "Station " + str(self.id) + ": " + self.steetName + " (" + str(self.get_slot_amount()) + " slots)"