"""
Logger class is used to log messages, which can be used to generate html logs.
This class is a singleton.
"""

import datetime


class Logger(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls.logs = []
        return cls._instance

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