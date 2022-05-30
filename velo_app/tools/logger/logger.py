"""
Logger class is used to log messages, which can be used to generate html logs.
"""

from datetime import datetime


class Logger():

    def __init__(self):
        self.logs = []

    def add_log(self, log_message):
        log = {"message": log_message, "time": datetime.now()}
        self.logs.append(log)

    def get_logs(self):
        return self.logs

    def generate_html(self):
        html = '<html><body>'
        for log in self.logs:
            html += f'<p>{log}</p>'
        html += '</body></html>'
        return html