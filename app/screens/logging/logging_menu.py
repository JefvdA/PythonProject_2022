from tools.menu_generator.menu import Menu
import tools.cli_tools.tools as cli_tools
import tools.html_generator.views.stations_list as station_list_html

import screens.main.main_menu as main_menu

from velo_app import VeloApp

options = [
    "Overviews of all stations",
    "Logs for a specific user",
    "Logs for a specific bike",
]

def run(app: VeloApp):
    menu = Menu(options) 

    correct_input = False
    while not correct_input:
        correct_input = True

        user_input = menu.get_user_input()
        cli_tools.clear()
        match user_input:
            case "1":
                stations = app.get_stations()
                station_list_html.run(stations)

                cli_tools.clear()
                print("Your static website has been generated. You can find it in the 'html' folder.")
                cli_tools.wait_for_enter()
            case _:
                print("Sorry that's not a correct option. Try again")
                cli_tools.wait_for_enter()
                correct_input = False

    main_menu.run(app)