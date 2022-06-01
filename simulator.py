"""
Simulator class, that is responsible of simulating the state of VeloApp.
Time multiplier can be set to slow down / speed up the simulation.

Default time multiplier is real-time 1 sec / 1 sec.

Every 5 seconds 1 user will take a bike / put a bike away.
    The action is chosen random (50/50), and a user is chosen based on the action (user with bike / without bike)

Every 10 seconds 1 transporter will take bikes from a full station (+75%) and fill an empty station (+25%).
"""

import datetime
import random
import threading
import time

import tools.cli_tools.tools as cli_tools


class Simulator:
    time = None
    seconds = 0

    def __init__(self, app, time_multiplier: str) -> None:
        self.app = app
        
        try:
            self.time_multiplier = int(time_multiplier)
        except:
            self.time_multiplier = 1

        self.simulation_live = False
        self.sim = threading.Thread(target=self.run_simulation)

    def start(self) -> None:
        Simulator.time = datetime.datetime.now()
        Simulator.seconds = 0

        if not self.simulation_live:
            self.simulation_live = True
            self.sim.start()
        
        cli_tools.wait_for_enter() 

        self.stop()

    def stop(self) -> None:
        if self.simulation_live:
            self.simulation_live = False
            self.sim.join()
        
        Simulator.time = None
        Simulator.seconds = 0
        
    def run_simulation(self) -> None:
        users = self.app.get_users()
        transporters = self.app.get_transporters()
        stations = self.app.get_stations()

        while self.simulation_live:
            cli_tools.clear()
            print(f"Simulation is running (x{self.time_multiplier}), press ENTER to stop it.")
            print(f"Elapsed time in the simulation: {str(datetime.timedelta(seconds=Simulator.seconds))}")

            if Simulator.seconds % 5 == 0: # Every 5 seconds 1 user will take a bike / put a bike away.
                self.do_user_action(users, stations)
            if Simulator.seconds % 10 == 0: # Every 10 seconds 1 transporter will take bikes from a full station (+75%) and fill an empty station (+25%).
                self.do_transporter_action(transporters, stations)

            time.sleep(1 / self.time_multiplier)
            Simulator.seconds += 1

    def do_user_action(self, users, stations) -> None:
        user_action_completed = False
        while not user_action_completed:
            station = stations.get_random_station()

            rng = random.randint(0, 100)
            if rng <= 50:
                user = users.get_random_user_with_bike()
                
                if user is not None:
                    user_action_completed = user.put_bike_away(station)
            else:
                user = users.get_random_user_without_bike()
                
                if user is not None:
                    user_action_completed = user.take_bike(station)

    def do_transporter_action(self, transporters, stations) -> None:
        transporter = transporters.get_random_user()
        