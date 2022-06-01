import datetime
"""
create a transaction object. Ensure to include transaction properties: date, type, status, details.
"""
class Transaction:
    def __init__(self,date,type,status,details):
        self.date = datetime.datetime()
        self.type = type
        self.status = status
        self.details = {}


def print(self):
    return self.__dict__