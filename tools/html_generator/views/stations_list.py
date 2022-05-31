from .. import generator

from repositories.stations import Stations

def run(stations: Stations):
    html = generate_html(stations)
    generator.generate_html_file("stations_list", "stations", html)

def generate_html(stations: Stations):
    """
    Generate HTML code for stations list.
    :param stations: Stations object
    :return: HTML code
    """
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>VeloApp</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
        <link rel="stylesheet" href="../../../css/style.css">
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h1>VeloApp</h1>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <h2>Stations</h2>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Name</th>
                                <th scope="col">Bikes</th>
                                <th scope="col">Slots</th>
                            </tr>
                        </thead>"""

    for station in stations.stations:
        html += f"""
            <tr>
                <th scope="row">{station.id}</th>
                <td>{station.streetName}</td>
                <td>{station.get_bike_count()}</td>
                <td>{station.get_total_slots()}</td>
            </tr>"""
    

    html += """
                        </table>
                </div>
            </div>
        </div>
    </body>"""

    return html