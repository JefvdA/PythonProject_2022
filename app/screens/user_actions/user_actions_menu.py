from tools.menu_generator.menu import Menu
import tools.cli_tools.tools as cli_tools

from screens.user_actions.local_screens import take_bike_menu
from screens.user_actions.local_screens import put_bike_away_menu

from classes.user import User
from velo_app import VeloApp


options = [
    "Take a bike from a station",
    "Put a bike away at a station"
]

def run(app: VeloApp, user: User):
    cli_tools.clear()

    if user.get_bike_count() == 0:
        take_bike_menu.run(app, user)
        return

    if user.get_bike_count() == user.get_max_bikes():
        put_bike_away_menu.run(app, user)
        return

    show_choice_menu(app, user)

def show_choice_menu(app: VeloApp, user: User):
    menu = Menu(options)

    correct_input = False
    while not correct_input:
        correct_input = True

        user_input = menu.get_user_input()
        cli_tools.clear()

        match user_input:
            case "1":
                take_bike_menu.run(app, user)
            case "2":
                put_bike_away_menu.run(app, user)
            case _:
                print("Sorry that's not a correct option. Try again")
                cli_tools.wait_for_enter()
                correct_input = False