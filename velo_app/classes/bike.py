class Bike:
    index = 0

    def __init__(self):
        Bike.index += 1
        self.id = Bike.index