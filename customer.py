from random import random

"""
Create a Customer. Ensure to include customer banking details such as: 
Account name, Account number is automatically generated, customer age,
customer gender, customer phone number, customer date of birth.
"""

class Customer:
    def __init__(self, name, phone_number,gender,date_of_birth):
        self.name = name
        self.phone = phone_number
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.account_number = random.randint(100000000,9999999999)# generate 10 digit random numbers
        self.balance = 0

    def send_money(self):
        pass
    def buy_airtime(self):
        pass
    def make_payments(self):
        pass
    def recieve_deposite(self):
        pass

    def print(self):
        return self.__dict__
