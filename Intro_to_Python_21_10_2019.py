# -*- coding: utf-8 -*-
"""
Fifteenth session

Created on Mon Oct 21 18:28:53 2019

@author: Basilio M.P.
"""

#########
# MODULES
#########

# Modules are a set of elements bundled together, as packages in R.

# In syntax 'numpy.random.normal()', the first word refers to the directory (numpy),
# the second word refers to the file (random), and the third one to the function (normal()).

# Building a python module using the computer terminal.
# Check the folder ml in this session's path to see this exercise.

# Terminal code
# =============================================================================
# mkdir ml
# cd ml
# touch __main__.py
# touch __init__.py
# touch regression.py
# =============================================================================


# Absolute 'import' is importing stating the complete path of the file or directory
# Relative imports are those in which only part of the path is stated, altough it works
# it is not advised given it is more confusing.

# Terminal code
# =============================================================================
# python3 -m ml 100 
# =============================================================================


# sys module
import sys
sys.argv

############
# EXCEPTIONS
############

# Exceptions allow Python to react when something unexpected occurs instead of
# failing with no alternative.

# try operator
# Example in which problems arise when the input received is not what we expect:
n = None
while n is None:
    try:
        n = input('Insert a number:')
        n = int(n)
    except:
        print('Not a number provided.') # Run the section and insert a character 
                                        # to see what happens.
        n = None
print('Everything continues without an error because the exception was set up!')
print(n)

# Another example in which we provide exceptions for different scenarios.
# Run the following section and see which error is prompted.
try:
    4 / 0
except ValueError:
    print('Error provoked by wrong value') 
except ZeroDivisionError:
    print('Error provoked by division by zero.')
finally:
    print("'finally' module is a piece of code that will be executed in any case.")
    
#################
# APIs and Pandas
#################

import pandas as pd
import requests

req = requests.request('GET', 'https://api.itbit.com/v1/markets/XBTUSD/ticker')
req # When successful, a code 200 is returned.

# Now the variable 'req' should store a JSON object with downloaded information.
# Consequently, we can format it with the method '.json'
# A useful website for checking JSON objets is jsonlint.com
req.json()

data = req.json()
type(data)

data['bid']

# New request asking for a set of days instead of a single record.
data = requests.request('GET', 'https://api.itbit.com/v1/markets/XBTUSD/trades?since=5CR1JEUBBM8B').json()

# Transforming the JSON object into a data frame
newdata = pd.DataFrame(data['recentTrades'])
# Some methods included in the object data frame:
newdata
newdata.describe()
# Maximum value for a given variable in the data frame
newdata['price'].max()

from matplotlib import pyplot as plt

newdata[['price']].plot()

### Further readings:
# Blog Pybonacci
# Module mysql
# Online courses: Coursera, udacity or edx
