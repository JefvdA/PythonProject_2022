from classes.user import User


class Transporter(User):
    index = 0

    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.id = Transporter.index
        self.MAX_BIKES = 10

        Transporter.index += 1