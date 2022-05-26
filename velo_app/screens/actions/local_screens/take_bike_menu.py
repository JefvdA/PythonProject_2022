import os

import tools.cli_tools.tools as cli_tools

from screens.actions.local_screens import station_list
from screens.login import login_menu

from classes.user import User
from velo_app import VeloApp


def run(app: VeloApp, user: User):
    cli_tools.clear()
    station_list.show(app)

    station_id = input("From which station do you want to take a bike? (Give station id) >>> ")
    cli_tools.clear()
    
    station = app.get_stations().get_stations()[int(station_id)]
    succes = user.take_bike(station)

    if succes:
        print(f'{user.get_name()} succesfully took a bike from {station.get_name()}')
    else:
        print(f'{user.get_name()} failed to take a bike from {station.get_name()}. There are no bikes available at this station.')
    cli_tools.wait_for_enter()

    login_menu.run(app)