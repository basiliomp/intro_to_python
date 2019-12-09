# -*- coding: utf-8 -*-
"""
Fourteenth session

Created on Thu Oct 17 18:45:52 2019

@author: Basilio
"""

################################
# OBJECT-ORIENTED PROGRAMMING II
################################

# Definition of a new class 'List'
class MyList(object):
    def __init__(self):
        self._size = 0
        self._elements = () # A tuple
    
    def length(self):
        return self._size
    
    def __len__(self):
        return self._size
    
    def add(self, new_element):
        self._elements += (new_element, ) # The new element is transformed into a tuple.
        self._size += 1

    def extract(self, position):
        for i, element in enumerate(self._elements): # Enumerate gives a number 
            if position == i:
                return element
            return IndexError('Index out of list boundaries.')
        
    def simmetry(self):
        i = 0
        j = -1
        for _ in range(len(self.elements)/2) - 1:
            return False


# Using the freshly created list class
l = MyList() # First MyClass object
MyList.length()

# PEP-8 Style guide

@property # decorators. Other two common decorators are: @classmethod and @staticmethod
# Decorators tell Python to run something before and something else after running 
# the function that is being called. (https://realpython.com/primer-on-python-decorators/)
__getitem__ # Special method.
_nameofthemethod # Private method, those with an underscore at the start.


############
# ASSIGNMNET
############
# Initial set up
n_doors = 3
iterations = 100
total_wins = 0

doors = [False] * n_doors # Creating a list of 3 'empty' of non-prized doors.

import random
for _ in range(iterations):
    prize_index = random.randint(0, 2)

    doors[prize_index] = True # Assigning the prize to the random index

    chosen_door = random.randint(0, n_doors - 1)

    #print(doors, chosen_door)

    did_i_win = doors[chosen_door]
    if did_i_win:
        total_wins += 1

print("Ratio of wins {}".format(total_wins / iterations))


# Second simulation with one opening before the final choice of door.
n_doors = 3
iterations = 100
total_wins = 0

doors = [False] * n_doors # Creating a list of 3 'empty' of non-prized doors.

import random
for _ in range(iterations):
    prize_index = random.randint(0, n_doors - 1) # From 0 to 2, both included.

    doors[prize_index] = True # Assigning the prize to the random index

    chosen_door = random.randint(0, n_doors - 1)
    #print(doors, chosen_door)
    host_door = random.randint(0, n_doors)
    while host_door != chosen_door and host_door != prize_index:
        host_door = prize_index = random.randint(0, n_doors)
        print(doors)
        print(chosen_door, host_door)
    
    if chosen_door == prize_index:
        host_door = 0 if chosen_door > 0 else 1
    else:
        host_door = 
    did_i_win = doors[chosen_door]

    # Checking     
    if did_i_win:
        total_wins += 1

print("Ratio of wins {}".format(total_wins / iterations))
