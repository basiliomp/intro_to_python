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

# Dictionary for translating from Spanish to Catalan
es2ca = {'hola': 'bones', 'llamo': 'dic', 'adios': 'adeu', 'mesa': 'taula',
         'silla': 'cadira', 'eso': 'aixo', 'me': 'em', 'calle': 'carrer',
         'un': 'un', 'perro': 'gos', 'ocho': 'vuit', 'te': 'et', 'hoy': 'avui',
         'es': 'es', 'gato': 'gat', 'algoritmo': 'algoritme'}

# Dictionary for translating from Spanish to English
es2en = {'hola': 'hello', 'nombre': 'name', 'adios': 'bye', 'mesa': 'table',
         'silla': 'chair', 'eso': 'this', 'me': 'my', 'calle': 'street',
         'un': 'a', 'perro': 'dog', 'ocho': 'eight', 'te': 'you', 'hoy': 'today',
         'es': 'is', 'gato': 'cat', 'algoritmo': 'algorithm', 'mi': 'my'}

def translate(sentence:str, dictionary:Dict[str, str]) -> str:
    sentence = sentence.split(' ')
    translated = ''
    for w in range(len(sentence)):
        if sentence[w].lower() in dictionary:
            translated += dictionary[sentence[w].lower()] + " "
        else:
            translated += sentence[w] + ' '
    return translated

# Using the new function for a Spanish sentence and the Catalan dictionary
translate("Hola me llamo María", es2ca)

# Using the new function for a Spanish sentence and the Catalan dictionary
translate("Hola mi nombre es John", es2en)

#############
# ASSIGNMENTS
#############

# Build a function for printing all the multiplication tables from 0 to a given number.
# Output should be a string: '1 x 1 = 1'.

def tables(until:int):
    tablestxt = open("my_text_file.txt", "wt")
    for i in range(until + 1):
        tablestxt.write(str(i) + "\n")
        #tablestxt.write(str(["Multiplication table for", i, ":"]))
        print("Multiplication table for", i, ":")
        for n in range(11):
            result = i * n
            tablestxt.write(str(result) + "\n")
            #tablestxt.write(str[(str(i) + " × " + str(n) + " = " + str(result) + "\n")])
            print(i, " × ", n, " = ", result)
    tablestxt.close()
    #return tablestxt
# Testing    
tables(3)

# Build an emulator for throwing darts to a dartboard.
# Each dart will have a value (x,y) in the two-dimensional space of the dartboard.
# Since the dartboard is a circle inside our two-dimensional space (a square),
# the ratio between the circle area and the square are will be similar to the
# proportion of darts hitting the dartboard and those hitting out of it.
# Assuming that darts are thrown randomly, following a uniform distribution across
# the dartboard, there will be a direct relation between the number of darts
# hitting inside and those hitting out of the circle.
import numpy as np
x = np.random.uniform(0, 1, 10000)
y = np.random.uniform(0, 1, 10000)
# Since the ratio between the area of the circle and the area of the square is
# equal to the number of 

### My sketchy answer
import matplotlib.pyplot as plt
plt.plot(x, y)

# Building a set of x-y pints.
xy = []
for i in range(len(x)):
    xy.append([x[i], y[i]])

# Assigning points in the x-y range to a list if they 'hit the dartboard'
dartboard = []
miss = []

for i in range(len(x)):
    if (xy[i][0] < 0.25):
        if (xy[i][1] < 0.25 or xy[i][1] > 0.75):
            dartboard.append(xy[i])
    elif (xy[i][0] > 0.75):
        if (xy[i][1] < 0.25 or xy[i][1] > 0.75):
            dartboard.append(xy[i])
    else:
        miss.append(xy[i])

len(dartboard) / len(xy)
len(miss) / len(xy)

mypi = (4 * (len(dartboard) / len(x))) / (len(dartboard) + len(miss))

# Testing the result. Is my calculus for pi actually any similar to pi?
import math
round(mypi, 4) == round(math.pi, 4)
print(mypi)

### Solving the exercise in class
COPY FROM NOTEBOOK

# Running over two lists in parallel with zip
for x[i], y[i] in zip(x, y):

