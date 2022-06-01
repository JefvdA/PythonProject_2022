import tools.cli_tools.tools as cli_tools

import screens.main.main_menu as main_menu

from velo_app import VeloApp
from simulator import Simulator


def run(app: VeloApp):
    cli_tools.clear()

    time_multiplier = cli_tools.get_user_input("Give the time multiplier (1 = real time, 2 = 2x real time, etc): ")
    
    simulator = Simulator(app, time_multiplier)
    simulator.start()

    main_menu.run(app)
