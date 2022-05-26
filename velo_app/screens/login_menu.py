import os

from tools.menu_generator.menu import Menu

from velo_app import VeloApp


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
                print("COMING SOON...")
                input("Press enter to continue...")
                os.system('clear')
            case "2":
                print("COMING SOON...")
                input("Press enter to continue...")
                os.system('clear')
            case _:
                print("Sorry that's not a correct option. Try again")
                input("Press enter to continue...")
                os.system('clear')
                correct_input = False