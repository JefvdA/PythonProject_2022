"""
Logger class is used to log messages
"""

from datetime import datetime


class Logger():

    def __init__(self):
        self.logs = []

    def add_log(self, log_message):
        log = Log(log_message)
        self.logs.append(log)

    def get_logs(self):
        return self.logs

class Log():
    
        def __init__(self, message):
            self.message = message
            self.time = datetime.now()
    
        def get_message(self):
            return self.message
    
        def get_time(self):
            return self.time