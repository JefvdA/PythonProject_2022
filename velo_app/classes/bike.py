class Bike:
    index = 0

    def __init__(self):
        self.id = Bike.index
        Bike.index += 1

    def get_id(self) -> int:
        return self.id