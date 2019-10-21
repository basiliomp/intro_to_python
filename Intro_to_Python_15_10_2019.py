# -*- coding: utf-8 -*-
"""
Twuelveth session

Created on Tue Oct 15 18:30:17 2019

@author: Basilio M. P.
"""

###################################
# OBJECT-ORIENTED PROGRAMMING (OOP)
###################################

# Any software program, is susceptible to be considered as an object.
# Each object has some attributes or features related to it.
# Those attributes can be different across specific examples (implementations) of the object.

# Class and objects
# A class is the abstraction of the object written in the software, while the object
# is the specific, existing object.

# Imagine a bank account as the class we are trying to abstract and program.
# What are the attributes of the bank account?
# Bank accounts can be defined acording to their date of creation, id, client id,
# balance, currency, account activity, and the possibility of attachment of the account (embargo).
# This class 'bank account' is the template for the different objects.

# Additionally, the class bank account we are trying to abstract for programming
# will need some functions in order to be useful. A proper bank account should 
# allow a functionality to be created and removed, then a way to be able to 
# receive money, transfer money, check the balance, check the account activity,
# and finally to offer some analysis of our account activity.

# In OOP atributes are the features defining the object, and shall not be accessible
# nor editable from outside the object. The way to interact with objects is through
# the methods. We can think of attributes as variables, and methods as functions.

# Other programming paradigms are:
# Imperative (sequential running), functional (scala, Haskel) or declarative (SQL).
# The task of designing classes, objects, and so on, is 'Software Engineering',
# a branch of Information Technologies.

# Importing the library datetime
from datetime import datetime
from typing import Tuple

# Creating the first class 'BankAccount'
class BankAccount(object):
    # Attributes definition. The name shoudld start with '_' so it is private.
    # The initial method should always be defined like this.
    def __init__(self,
                 iban:str,
                 currency:str = 'Eur'): # If there are any attribute with default values,
                                        # they must be listed at the end.
        print('This is the __init__')
        self._iban = iban
        self._client_id = None
        self._date = datetime.now()
        self._balance = 0.  # The dot creates a float number.
        self._currency = currency
        self._activity = []
        self._amountattachment = 0.
        print('Everything is initialized.')
    
    # Methods definition
    def check_iban(self) -> str:
        return self._iban
    
    def check_client_id(self) -> str:
        return self._client_id
    
    def create(self, client_id: int) -> None:
        self._clients.append(client_id)
        self._activity.append('{} [CREATION] Client: {}'.format(datetime.now(), client_id))
    
    def check_activity(self):
        for action in self._activity:
            print(action)
    
    def check_balance(self, currency='Eur') -> Tuple[float, str]:
        """ Returns the account balance using the stated currency."""
        return self._balance

    def add_money(self, amount: float) -> None:
        self._balance += amount
        self._activity.append('{} [ADITION] Client: {}'.format(datetime.now(), amount))
    
    def withdraw_money(self, amount: float) -> None:
        assert amount <= self._balance, 'Amount of money unavailable: balance exceeded.'
        self._balance -= amount
        self._activity.append('{} [WITHDRAWAL] Client: {}'.format(datetime.now(), amount))

    def transfer(self, amount: float, account: 'BankAccount') -> None:
        self.withdraw_money(amount)
        account.add_money(amount)


# Creating the first bank account (object)
account_Mary = BankAccount(iban = 'US_0987')
account_Mary.add_money(100) #Adding 100 to the balance.
account_Mary.check_balance()

# Creating a second bank account (object)
account_Eric = BankAccount(iban = "ES_0110")
account_Eric.add_money(5) #Adding 5 to the balance.
account_Eric.check_balance()

# Transfering 30 € from Mary's account to Eric.
account_Mary.transfer(30, account_Eric)
# Balance of Eric increased by 30
account_Eric.check_balance()
# Balance of Mary decreased by 30
account_Mary.check_balance()

account_Mary.check_activity()
# Trying to transfer more money than we have in the account.
account_Mary.transfer(500, account_Eric)
# The balances should remain the same, because there is not enough money available.

# Building a new class for users
class User(object):
    
    def __init__(self, client_id: int, nick: str, password: str):
        self._client_id = client_id
        self._nick = nick
        self._password = password
    
    def validation(self, nick: str, password: str) -> bool:
        return self._nick == nick and self._password == password
    
    def check_nick(self) -> str:
        return self._nick
    
    def check_client_id(self) -> str:
        return self._client_id


# Building another class for ATMs:
from typing import List

class ATM(object):
    # Attributes
    def __init__(self, accounts: List[BankAccount], users: List[User],
                 n_10: int, n_20: int, n_50: int, n_100:int): #Number of notes of each type
        self._accounts = None
        self._n_10 = n_10 
        self._n_20 = n_20
        self._n_50 = n_50
        self._n_100 = n_100
        self._active_user = None
        self._active_account = None
        self._accounts = accounts
        # Users will be stored in a dictionary in which 
        # key: nick => value: obj from the user to validate.
        self._users = {}
        for user in users:
            self._users[user.check_nick()] = user

    # Methods
    def log_in(self, nick:str, password: str):
        if nick in self._users:
            # All right
            u = self._users[nick]
            if u.validation(nick, password):
                print("Welcome {}.".format(nick))
                self._active_user = u.check_client_id()
                for account in self._accounts:
                    if account.check_client_id() == u.check_client_id():
                        self._active_account = account
                        break
                    
                self._active_account = u.check_client_id()
#+++++        
            else:
                raise ValueError("Invalid password.")
        else: 
            raise ValueError('Nick provided doesn\'t exist.')
            
    def check_active_user(self):
        return self._active_user()
    
    def log_out(self):
        self._active_user = None
        self._active_account = None
    
    def save(self, amount: float):
        assert self._active_user is not None, 'No user logged.'
        assert self._active_account is not None, 'No user logged.'
        self._active_account.add_money(amount)

    def check_balance():
        assert self._active_user is not None, 'No user logged.'
        assert self._active_account is not None, 'No user logged.'
        print(self._active_account.check_balance())
        
    def check_activity(self):
        assert self._active_user is not None, 'No user logged.'
        assert self._active_account is not None, 'No user logged.'
        for activity in self._active_account.check_activity():
            print('[]')
            print("")

    def transfer(self, amount: float, iban: str) -> None:
        assert self._active_user is not None, 'No user logged.'
        assert self._active_account is not None, 'No user logged.'
        for account in self._accounts:
            if BankAccount.check_iban() == iban:
                self._active_account.transfer(amount = amount, account = account)

# METHOD that reports the exchange rate for different currencies. Note that this method
# has no call to self! It is because it does not depend on any of the class attributtes.
@staticmethod # decorator. Other two common decorators are: @classmethod and @property
def exch_rate(currency_a = str, currency_b = str) -> float:
    if currency_a == 'Eur' and currency_b == 'USD':
        return 1.2
    if currency_a == 'Eur' and currency_b == 'BTC':
        return 1 / 7200
    if currency_a == 'USD' and currency_b == 'Eur':
        return 0.8
    if currency_a == 'USD' and currency_b == 'BTC':
        return 1 / 5400
    
#
u1 = User('0001', 'Martin', '1234')
u2 = User('0003', 'Pep', 'passs')
u3 = User('0059', 'Laura', 'qwerty')

ATM1 = ATM(accounts = [], users = [u1, u2, u3], n_10 = 1, n_20 = 2, n_50 = 3, n_100 = 4)
# Testing with a user unregistered.
ATM1.log_in(nick = "UnknownUser", password = "1234")
# Testing with a user registered but wrong password.
ATM1.log_in(nick = "Laura", password = "a")
# Testing a successful login.
ATM1.log_in(nick = "Laura", password = "qwerty")

# Laura has no money, so the transfer should call BankAccount.tranfer(), and this
# should call BankAccount.withdraw() , and this will raise an error.
ATM1.transfer(30, '0001')

# ASSIGNMENT

# Add new methods or modify the existing ones so ATM operations take into account notes in the machine.


# Build a 'list' class, considering which attributes and methods it should have.

    
#############
# INHERITANCE   
#############   

class CreditAccount(BankAccount):
    def __init__(self, iban: str, credit_limit: float): #
        super().__init__(iban)      # This line is indicating
        self._credit_limit(credit_limit)
        
    def withdraw_money(self, amount: float) -> None:  # Overriding methods! This new method
        assert amount <= self._balance + self._credit_limit, 'Amount of money unavailable: balance exceeded.'
        self._balance -= amount
        self._activity.append('{} [WITHDRAWAL] Client: {}'.format(datetime.now(), amount))

# Testing out new classes
credit1 = CreditAccount(iban = 'FR_0001', credit_limit = 5000.1)

    
    
    
    
    