from tools.menu_generator.menu import Menu
import tools.cli_tools.tools as cli_tools

import screens.login.local_screens.user_login_menu as user_login_menu
import screens.login.local_screens.transporter_login_menu as transporter_login_menu

from velo_app import VeloApp


options = [
    "Log in as a user",
    "Log in as a transporter"
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
                user_login_menu.run(app)
            case "2":
                transporter_login_menu.run(app)
            case _:
                print("Sorry that's not a correct option. Try again")
                cli_tools.wait_for_enter()
                correct_input = False