#! /usr/bin/env python3

'''
Project python 2022
Jef van der Avoirt - ITSOF1
'''


import os
import sys

from constants import VELO_PICKLE
from velo_app import VeloApp
from simulator import Simulator
import screens.initialize_menu as init_menu
import screens.main.main_menu as main_menu


def main():
    app = VeloApp()
    
    # Initiliaze the data
    if(not os.path.exists(VELO_PICKLE)): # If there is no data yet, start fresh
        app.initialize()
    else: # If saved data is found, ask user what to do
        os.system('clear')
        init_menu.run(app)

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "-s":
            if len(sys.argv) > 2:
                time_multiplier = int(sys.argv[2])
            else:
                time_multiplier = 1
            simulator = Simulator(app, time_multiplier)
            simulator.start()
    else:  
        main_menu.run(app)
    
    app.save_data() # App is closing, save data

if __name__ == "__main__":
    main()