import os

from screens.actions.local_screens import station_list
from screens.login import login_menu

from classes.user import User
from velo_app import VeloApp


def run(app: VeloApp, user: User):
    os.system('clear')

    show_bike_list(user)
    os.system('clear')

    station_list.show(app)
    station_id = input("At what station do you want to leave your bike? (Give station id) >>> ")
    station = app.get_stations().get_stations()[int(station_id)]

    user.put_bike_away(station)

    os.system('clear')
    print(f'{user.get_name()} succesfully put a bike away at {station.get_name()}')
    input("Press enter to continue...")
    os.system('clear')

    login_menu.run(app)

def show_bike_list(user: User):
    print(f'You are currently riding {user.get_bike_amount()} bikes, out of {user.get_max_bikes()}')
    print("""BIKES:\n
    ____________________""")

    bikes = user.get_bikes()
    for bike in bikes:
        print(f'Bike nr: {bike.get_id()}')

    input("Press enter to continue...")