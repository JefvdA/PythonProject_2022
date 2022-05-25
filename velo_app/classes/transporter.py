from classes.user import User


class Transporter(User):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.MAX_BIKES = 10