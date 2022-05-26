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
        init_menu.run(app)
    
    print(app)
    app.save_data()

if __name__ == "__main__":
    main()