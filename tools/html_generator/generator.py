import os
from constants import HTML_DIR

from repositories.stations import Stations

def generate_html_file(file_name, dir_name, html):
    """
    Generate HTML file.
    :param html: HTML code
    :return: None
    """

    dir = f"{HTML_DIR}/{dir_name}/"

    if not os.path.exists(dir): # Create directory if it doesn't exist
        os.makedirs(dir)

    with open(f"{dir}/{file_name}.html", 'w') as f:
        f.write(html)