class Bike:
    index = 0

    def __init__(self):
        self.id = Bike.index
        Bike.index += 1