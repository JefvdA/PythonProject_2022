import os

from tools.menu_generator.menu import Menu

from screens.actions import action_menu

from classes.user import User
from velo_app import VeloApp


options = [
    "Login with id",
    "Login with full name",
]

def run(app: VeloApp):
    menu = Menu(options)

    user: User = None

    correct_input = False
    while not correct_input:
        correct_input = True

        user_input = menu.get_user_input()
        os.system('clear')

        show_transporter_list(app)
        match user_input:
            case "1":
                user_id = input("Enter the id >>> ")
                user = app.get_transporters().get_user_by_id(int(user_id))
            case "2":
                user_name = input("Enter the full name >>> ")
                user = app.get_transporters().get_user_by_name(user_name)
            case _:
                print("Sorry that's not a correct option. Try again")
                input("Press enter to continue...")
                os.system('clear')
                correct_input = False
    
    if user is None:
        run(app)
    else:
        action_menu.run(app, user)

def show_transporter_list(app: VeloApp):
    transporters = app.get_transporters().get_users()
    print("""TRANSPORTERS:\n
    ____________________""")
    for transporter in transporters:
        print(transporter)