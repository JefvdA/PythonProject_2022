#! /usr/bin/env python3

'''
Project python 2022
Jef van der Avoirt - ITSOF1
'''


import os

from constants import VELO_PICKLE
from velo_app import VeloApp
import screens.initialize_menu as init_menu


def main():
    app = VeloApp()
    
    if(not os.path.exists(VELO_PICKLE)):
        app.initialize()
    else:
        correct_input = False
        while not correct_input:
            correct_input = True

            user_input = init_menu.get_user_choice()
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
    
    print(app.get_users().get_user_count())
    app.save_data()

if __name__ == "__main__":
    main()