import json
import random

from classes.user import User

FIRSTNAMES_JSON = "assets/first-names.json"
LASTNAMES_JSON = "assets/last-names.json"


class Users:
    def __init__(self) -> None:
        self.users = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def get_users(self):
        return self.users

    def generate_users(self, amount):
        # TODO: Move to seperate module
        # With the 5493 firstnames and 88798 lastnames -> 5493*88798 = 487.767.414 possible combinations
        firstnames = []
        lastnames = []
        with open(FIRSTNAMES_JSON) as json_file: 
            firstnames = json.load(json_file)
        with open(LASTNAMES_JSON) as json_file:
            lastnames = json.load(json_file)

        for i in range(amount):
            firstname = random.choice(firstnames)
            lastname = random.choice(lastnames)
            user = User(firstname, lastname)
            self.add_user(user)

    def __str__(self) -> str:
        string = ""
        for user in self.users:
            string += str(user) + "\n"
        return string