import tools.cli_tools.tools as cli_tools

from screens.user_actions.local_screens import station_list
import screens.main.main_menu as main_menu

from classes.user import User
from velo_app import VeloApp


def run(app: VeloApp, user: User):
    cli_tools.clear()

    show_bike_list(user)

    station_list.show(app)
    station_id = input("At what station do you want to leave your bike? (Give station id) >>> ")
    cli_tools.clear()

    station = app.get_stations().get_stations()[int(station_id)]
    succes = user.put_bike_away(station)

    if succes:
        print(f'{user.get_name()} succesfully put a bike away at {station.get_name()}')
    else:
        print(f'{user.get_name()} failed to put a bike away at {station.get_name()}. There are no free slots at this station.')
    cli_tools.wait_for_enter()

    main_menu.run(app)

def show_bike_list(user: User):
    print(f'You are currently riding {user.get_bike_amount()} bikes, out of {user.get_max_bikes()}')
    print("""BIKES:\n
    ____________________""")

    bikes = user.get_bikes()
    for bike in bikes:
        print(f'Bike nr: {bike.get_id()}')

    cli_tools.wait_for_enter()