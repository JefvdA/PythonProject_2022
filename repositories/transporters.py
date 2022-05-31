from classes.transporter import Transporter
from repositories.users import Users


class Transporters(Users):
    def add_user(self, firstname, lastname):
        self.users.append(Transporter(firstname, lastname))