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

#########
# MODULES
#########

# Modules are a set of elements bundled together, as packages in R.

# In syntax 'numpy.random.normal()', the first word refers to the directory (numpy),
# the second word refers to the file (random), and the third one to the function (normal()).

############
# ASSIGNMNET
############

# Build a program to run an iteration over the Monty Hall game, then execute it
# several times keepig the initial choice, and then switching boxes. This way you
# will test the results.


