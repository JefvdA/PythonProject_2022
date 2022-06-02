from tools.menu_generator.menu import Menu
import tools.cli_tools.tools as cli_tools

from velo_app import VeloApp


options = [
    "Load data",
    "Start fresh"
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
                app.load_data()
            case "2":
                app.initialize()
            case _:
                print("Sorry that's not a correct option. Try again")
                cli_tools.wait_for_enter()
                correct_input = False