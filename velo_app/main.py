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
    app = VeloApp() ## Initilize the app object
    
    # Initiliaze the data
    if(not os.path.exists(VELO_PICKLE)): # If there is no data yet, start fresh
        app.initialize()
    else: # If saved data is found, ask user what to do
        init_menu.run(app)
    
    print(app)
    app.save_data()

if __name__ == "__main__":
    main()