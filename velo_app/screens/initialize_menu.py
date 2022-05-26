import os

from tools.menu_generator.menu import Menu

from velo_app import VeloApp


options = [
    "Load data",
    "Start fresh"
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
                app.load_data()
            case "2":
                os.system('clear')
                app.initialize()
            case _:
                print("Sorry that's not a correct option. Try again")
                input("Press enter to continue...")
                os.system('clear')
                correct_input = False