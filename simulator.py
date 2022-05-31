"""
Simulator class, that is responsible of simulating the state of VeloApp.
Time multiplier can be set to slow down / speed up the simulation.

Default time multiplier is real-time 1 sec / 1 sec.

Every second 1 user will take a bike / put a bike away.
    What user, will be random, and the action is determined by if it already has a bike or not.

Every 5 seconds 1 transporter will take bikes from a full station (+75%) and fill an empty station (+25%).
"""

import random
import threading
import time

from repositories.stations import Stations
from repositories.users import Users
from repositories.transporters import Transporters

from classes.user import User
from classes.station import Station
from classes.transporter import Transporter

from velo_app import VeloApp


class Simulator:
    def __init__(self, app: VeloApp, time_multiplier: int) -> None:
        self.app = app
        
        if time_multiplier is "":
            self.time_multiplier = 1
        else:
            self.time_multiplier = time_multiplier

        self.simulation_live = False
        self.sim = threading.Thread(target=self.run_simulation)

    def start(self) -> None:
        if not self.simulation_live:
            self.simulation_live = True
            self.sim.start()

    def stop(self) -> None:
        if self.simulation_live:
            self.simulation_live = False
            self.sim.join()
        
    def run_simulation(self) -> None:
        users: Users = self.app.get_users()
        transporters: Transporters = self.app.get_transporters()
        stations: Stations = self.app.get_stations()

        seconds = 0
        while self.simulation_live:
            if seconds >= 5:
                transporter: Transporter = transporters.get_random_user()
                self.do_transporter_action(transporter, stations)
                seconds = 0

            self.do_user_action(users, stations)

            time.sleep(1 / self.time_multiplier)
            seconds += 1

    def do_user_action(self, users: Users, stations: Stations) -> None:
        user_action_completed = False
        while not user_action_completed:
            station: Station = stations.get_random_station()

            rng = random.randint(0, 100)
            if rng <= 50:
                user: User = users.get_random_user_with_bike()
                
                if user is not None:
                    user_action_completed = user.put_bike_away(station)
            else:
                user: User = users.get_random_user_without_bike()
                
                if user is not None:
                    user_action_completed = user.take_bike(station)

        print(f"{user.get_name()} took a bike from station {station.get_name()}.")

    def do_transporter_action(self, transporter: Transporter, stations: Stations) -> None:
        pass
        