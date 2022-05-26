from classes.user import User
import tools.name_generator.generator as name_generator


class Users:
    def __init__(self) -> None:
        self.users = []
    
    def add_user(self, firstname, lastname):
        self.users.append(User(firstname, lastname))
    
    def get_users(self):
        return self.users

    def get_user_count(self):
        return len(self.users)

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