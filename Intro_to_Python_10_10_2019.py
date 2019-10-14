# -*- coding: utf-8 -*-
"""
Tenth session

Created on Thu Oct 10 18:35:36 2019

@author: Basilio M.P.
"""

#############
# Polimorfism (default arguments in functions)
#############

# Setting a default value for an argument, that does not need to be specified as a result is
# as simple as assigning it inside initial parenthesis in the function definition.
def mult_table_stop(n: int, stop: int=10) -> None: # stop will be 10, unless specified otherwise.
    a = n
    print('== {}'.format(a), '=' * 50)
    for b in range(stop + 1):
        c = a * b
        print('{} X {} = {}'.format(a, b, c))

mult_table_stop(2) # stop will be 10, unless specified otherwise.

# IN OTHER PROGRAMMING LANGUAGES, this is achieved through the following scheme:
# This would be the general case function (2 arguments).
def mult_table_stop(n: int, stop: int) -> None:
    a = n
    print('== {}'.format(a), '=' * 50)
    for b in range(stop + 1):
        c = a * b
        print('{} X {} = {}'.format(a, b, c))
# This the specific case that will be most used, and therefore can be called without specifying one argument.
def mult_table_stop(n: int) -> None:
    mult_table_stop(n, 10)

########################
# NON DECLARED ARGUMENTS
########################

# Use an asterisk to identify the open argument that could take the function.
def summatory(a: int, b: int, *args) -> int:
    print('a', a)
    print('b', b)
    print('args', args)
    return a + b + sum(args)

# Testing
summatory(2, 1) # No undeclared arguments
summatory(2, 1, 3) # One undeclared arguments
summatory(2, 1, 3, 10) # Multiple undeclared arguments. Python is building a tuple for them.

# It is possible to alter the order in which we declare arguments in a function
# by naming them explicitely.
def exponen(base: int, power: float) -> float:
    return base ** power
exponen(2, 3)
exponen(power=3, base=2) # Instead of the default order like in the line above.

# KWARGS or key word arguments
# Silly example to see how to use these undeclared arguments.
def draw_line(x0, x1, y0, y1, **kwargs):
    print(x0, x1, y0, y1)
    print(kwargs)

draw_line(0, 1, 0, 1) #Calling the functions using the declared arguments only.
draw_line(0, 1, 0, 1, line_width=5) #Here we provide an extra argument as kwarg.
draw_line(0, 1, 0, 1, line_width=5, line_color='#ff00000f')


###########
# LIBRARIES
###########

# Check all the libraries installed in the conda session
!conda list

# Importing libraries, i.e. loading them in the current session
import numpy

# The convention is importing the numpy library with the name np (as 'np')
import numpy as np

# Using our first function from numpy to generate a series of 4 randon numbers
np.random.uniform(low=0, high=1, size=4)

# The function 'ranint' is also available for series of integer numbers.
np.random.randint(low=0, high=10, size=4)

from matplotlib import pyplot as plt

fig, ax = plt,subplots(1, 1, figsize=(6, 3))
ax.hist(np.random.randint(0, 10, 20), bins = 10)
plt.show()

# Another examples
x = np.random.uniform(0, 1, 10000)
y = np.random.uniform(0, 1, 10000)

fig, ax = plt.subplots()
ax.scatter(x, y)
fig.show()


fig, ax = plt.subplots()
ax.scatter(x, y, alpha = 0.1)
fig.show()

# Running over two lists in parallel with zip
for x[i], y[i] in zip(x, y):

###############
# MORE ON LOOPS: Break and continue
###############

# Example of a loop that would benefit from stopping once a defining situation has been reached.

# This first loop will go over all elements in the range(2,n), even when
# we already know a number is not a prime.  
n = 10
for i in range(2, n):
    is_prime = True
    if n % i == 0:
        print(i)
        is_prime = False
print(i, is_prime)

# Using 'break' we can avoid all those evaluations, saving time and energy in doing so.
for i in range(2, n):
    if n % i == 0:
        print(i)
        is_prime = False
        break
print(i, is_prime)

# Continue
n = 10
is_prime = True
for i in range(2, n):
    print(i)
    if n % i == 0:
        is_prime = False
        continue
    print('Is not divisible by {}'.format(i))
print(is_prime)

# Another situation in which to use continue
is_prime = True
for i in range(0, n):
    if i == 0:
        continue
    print(i / i ** 2)


    