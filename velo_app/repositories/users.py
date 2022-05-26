import tools.name_generator.generator as name_generator

from classes.user import User


class Users:
    def __init__(self) -> None:
        self.users = []
    
    def add_user(self, firstname, lastname):
        self.users.append(User(firstname, lastname))
    
    def get_users(self):
        return self.users

    def get_user_count(self):
        return len(self.users)

    def get_user_by_id(self, id: int) -> User:
        if id >= len(self.users) or id < 0:
            return None

        return self.users[id]

    def get_user_by_name(self, name: str) -> User:
        for user in self.users:
            if user.get_name() == name:
                return user
                
        return None

    def generate_users(self, amount):
        names = name_generator.generate_names(amount)
        for i in range(amount):
            name = names[i]
            firstname = name.split(" ")[0]
            lastname = name.split(" ")[1]
            self.add_user(firstname, lastname)

    def __str__(self) -> str:
        string = ""
        for user in self.users:
            string += str(user) + "\n"
        return string