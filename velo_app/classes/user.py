class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.bikes = []
        self.MAX_BIKES = 1

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName