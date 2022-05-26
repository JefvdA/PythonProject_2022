import os
from classes.station import Station
from classes.user import User

from screens.actions.local_screens import station_list
from screens.login import login_menu

from velo_app import VeloApp


def run(app: VeloApp, user: User):
    os.system('clear')
    station_list.show(app)

    station_id = input("From which station do you want to take a bike? (Give station id) >>> ")
    station = app.get_stations().get_stations()[int(station_id)]

    bike = station.take_bike_from_slot()
    user.take_bike(bike)

    os.system('clear')
    print(f'{user.get_name()} succesfully took a bike from {station.get_name()}')
    input("Press enter to continue...")
    os.system('clear')

    login_menu.run(app)