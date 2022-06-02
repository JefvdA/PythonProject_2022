from velo_app import VeloApp


def show(app: VeloApp):
    print("""STATIONS:\n
    ____________________""")

    stations = app.get_stations().get_stations()
    for station in stations:
        print(station)