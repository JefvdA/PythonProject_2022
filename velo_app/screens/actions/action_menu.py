import os
from classes.user import User

from velo_app import VeloApp


def run(app: VeloApp, user: User):
    os.system('clear')
    print(f"Welcome to the VeloApp | {user}")