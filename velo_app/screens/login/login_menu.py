import os

from tools.menu_generator.menu import Menu

from velo_app import VeloApp
import screens.login.local_screens.user_login_menu as user_login_menu


options = [
    "Log in as a user",
    "Log in as a transporter"
]

def run(app: VeloApp):
    menu = Menu(options)

    correct_input = False
    while not correct_input:
        correct_input = True

        user_input = menu.get_user_input()
        match user_input:
            case "1":
                os.system('clear')
                user_login_menu.run(app)
            case "2":
                print("COMING SOON...")
                input("Press enter to continue...")
                os.system('clear')
            case _:
                print("Sorry that's not a correct option. Try again")
                input("Press enter to continue...")
                os.system('clear')
                correct_input = False