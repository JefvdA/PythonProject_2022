class User:
    index = 0

    def __init__(self, first_name, last_name) -> None:
        self.id = User.index
        self.first_name = first_name
        self.last_name = last_name
        self.bikes = []
        self.MAX_BIKES = 1
        User.index += 1

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name