import os
from velo_app import VeloApp


def show_menu():
    message = """Saved data has been found, what do you want to do?\n
    1. Load data
    2. Start fresh"""
    print(message)

def get_user_input() -> str:
    show_menu()

    user_input = input("Give the number of your choice >>> ")
    return user_input

def run(app: VeloApp):
    correct_input = False
    while not correct_input:
        correct_input = True

        user_input = get_user_input()
        match user_input:
            case "1":
                app.load_data()
            case "2":
                app.initialize()
            case _:
                print("Sorry that's not a correct option. Try again")
                input("Press enter to continue...")
                os.system('clear')
                correct_input = False