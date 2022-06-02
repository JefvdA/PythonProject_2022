from tools.menu_generator.menu import Menu
import tools.cli_tools.tools as cli_tools

import screens.login.login_menu as login_menu
import screens.logging.logging_menu as logging_menu
import screens.simulation.simulation_menu as simulation_menu

from velo_app import VeloApp


options = [
    "Log in",
    "Generate logs",
    "Start simulation",
    "Exit"
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
                login_menu.run(app)
            case "2":
                logging_menu.run(app)
            case "3":
                simulation_menu.run(app)
            case "4":
                pass
            case _:
                print("Sorry that's not a correct option. Try again")
                cli_tools.wait_for_enter()
                correct_input = False