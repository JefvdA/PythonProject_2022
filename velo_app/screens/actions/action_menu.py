import os

from tools.menu_generator.menu import Menu

from screens.actions.local_screens import take_bike_menu
from screens.actions.local_screens import put_bike_away_menu

from classes.user import User
from velo_app import VeloApp


options = [
    "Take a bike from a station",
    "Put a bike away at a station"
]

def run(app: VeloApp, user: User):
    os.system('clear')

    if user.get_bike_amount() < user.get_max_bikes():
        take_bike_menu.run(app, user)
        return

    if user.get_bike_amount() > 0:
        put_bike_away_menu.run(app, user)
        return

    show_choice_menu(app, user)

def show_choice_menu(app: VeloApp, user: User):
    menu = Menu(options)

    correct_input = False
    while not correct_input:
        correct_input = True

        user_input = menu.get_user_input()
        os.system('clear')

        match user_input:
            case "1":
                take_bike_menu.run(app, user)
            case "2":
                put_bike_away_menu.run(app, user)
            case _:
                os.system('clear')
                print("Sorry that's not a correct option. Try again")
                input("Press enter to continue...")
                os.system('clear')
                correct_input = False