"""
Logger class is used to log messages
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