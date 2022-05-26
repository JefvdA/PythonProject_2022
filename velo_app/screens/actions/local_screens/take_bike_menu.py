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
    bike = station.take_bike_from_slot()
    user.take_bike(bike)

    print(f'{user.get_name()} succesfully took a bike from {station.get_name()}')
    cli_tools.wait_for_enter()

    login_menu.run(app)