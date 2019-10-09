# -*- coding: utf-8 -*-
"""
Ninth session

Created on Wed Oct  9 18:37:57 2019

@author: Basilio
"""
##############
# DICTIONARIES
##############

# Dictionaries link a key to a value

# Both the key and the value can be of different types:
# Keys must be 'hashable', while values can be any type of data.
# Dictionaries do not have an order for slicing.

my_dictio = {'one': 1}

my_dictio['one']

my_dictio[0] #This should bring an error.

my_dictio = {'one': 1,
             'two': 2}

# Values in dictionaries can be dictionaries too, so dictionaries can store dictionaries.
inventory = {111: {'es': 'Pan', 'pt': 'Pão', 'en': 'Bread', 'ca': 'Pa'},
             222: {'es': 'Carne', 'pt': 'Carne', 'en': 'Meat', 'ca': 'Carn'} }

inventory[111]

inventory[111]['pt']

# But values are not restricted to a given type:
inventory = {111: {'es': 'Pan', 'pt': 'Pão', 'en': 'Bread', 'ca': 'Pa'},
             222: {'es': 'Carne', 'pt': 'Carne', 'en': 'Meat', 'ca': 'Carn'},
             999: 'Not found',
             000: 0}

# Checking if there is anythin already assigned for a key:
111 in inventory # Is this key in the dictionary? The answer is of boolean type.
'en' in inventory[222] # IS there an English translation for product 222 ?

# Removing a key and its value:
del inventory[999]

# Reassining a new key to an existing value (in 2 steps, because we need to
# replicate the existing key-value pair, and then remove the old one).

inventory[444] = inventory[222]
del inventory[222]

# Exercise: Build a translation function using a dictionary
from typing import List, Dict

es2ca = {'hola' : 'bones', 'me' : 'em', 'llamo' : 'dic', 'gato' : 'gat' }
### COPY ES2CT SPANISH TO CATALAN DICTIONARY FROM CLASS NOTES

def translate(sentence:str, dictionary:Dict[str, str]) -> str:
    sentence = sentence.split(' ')
    translated = ''
    for w in range(len(sentence)):
        if sentence[w].lower() in dictionary:
            translated += dictionary[sentence[w].lower()] + " "
        else:
            translated += sentence[w] + ' '
    return translated

translate("Hola me llamo Pepe", es2ca)

#############
# ASSIGNMENTS
#############

# Build a function for printing all the multiplication tables from 0 to a given number.
# Output should be a string: '1 x 1 = 1'.

def tables(int):
    pass

# Build an emulator for throwing darts to a dartboard.
# Each dart will have a value (x,y) in the two-dimensional space of the dartboard.
# Since the dartboard is a circle inside our two-dimensional space (a square),
# the ratio between the circle area and the square are will be similar to the
# proportion of darts hitting the dartboard and those hitting out of it.
# Assuming that darts are thrown randomly, following a uniform distribution across
# the dartboard, there will be a direct relation between the number of darts
import numpy as np
x = np.random.uniform(0, 1, 10000)
y = np.random.uniform(0, 1, 10000)
# hitting inside and those hitting out of the circle.
# Since the ratio between the area of the circle and the area of the square is
# equal to the number of 





















