from .. import generator

from classes.station import Station

def run(station: Station):
    html = generate_html(station)
    generator.generate_html_file(f"station_{station.get_id()}", "stations/logs", html)

def generate_html(station: Station):
    """
    Generate HTML code for all logs of a station.
    :param stations: Stations object
    :return: HTML code
    """
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>VeloApp</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
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
                    <h2>Station {station.get_name()}</h2>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th scope="col">Time</th>
                                <th scope="col">message</th>
                            </tr>
                        </thead>
    """

    for log in station.get_logger().get_logs():
        html += f"""
        <tr>
            <th scope="row">{log.get_time()}</th>
            <td>{log.get_message()}</td>
        </tr>
        """
    
    html += """
                        </table>
                </div>
            </div>
        </div>
    </body>"""

    return html