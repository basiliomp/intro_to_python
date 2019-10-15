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
        self._clients = []
        self._date = datetime.now()
        self._balance = 0.  # The dot creates a float number.
        self._currency = currency
        self._activity = []
        self._amountattachment = 0.
        print('Everything is initialized.')
    
    # Methods definition
    def check_iban(self) -> str:
        return self._iban
    
    def create(self, client_id: int) -> None:
        self._clients.append(client_id)
        self._activity.append('{} [CREATION] Client: {}'.format(datetime.now(), client_id))
    
    def check_activity(self):
        for action in self._activity:
            print(action)
    
    def check_balance(self, currency='Eur') -> Tuple[float, str]:
        """ Returns the account balance using the stated currency."""
        return self._activity

# Creating the first bank account (object)
account_Mary = BankAccount(iban = 'US_0987', currency = 'USD')
account_Mary.check_balance()
    
# ASSIGNMENT

# Build a METHOD that reports the transaction rate for different currencies.

# Build a 'list' class, considering which attributes and methods it should have.

    
    
    
    
    
    
    
    
    
    
    