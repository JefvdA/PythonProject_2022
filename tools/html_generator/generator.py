from constants import HTML_DIR

from repositories.stations import Stations

def generate_html_file(file_name, dir_name, html):
    """
    Generate HTML file.
    :param html: HTML code
    :return: None
    """
    with open(f"{HTML_DIR}/{dir_name}/{file_name}", 'w') as f:
        f.write(html)