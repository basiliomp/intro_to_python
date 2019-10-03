# -*- coding: utf-8 -*-
"""
Fith session

Created on Wed Oct  2 19:06:36 2019

@author: Basilio M.P.
"""

#############
# COMPACT IFs
#############

# 'If' example
n = 3
if n % 2 == 0:
    s = "even number"
else:
    s = "odd number"
print(s)

s = "even number" if n % 2 == 0 else "odd number"
print(s)

n = 2
s = "even number" if n % 2 == 0 else "odd number"
print(s)

#############
# WHILE LOOPS
#############

# while condition:
#    instructions
i = 0
while i < 5:
    print(i)
    i += 1
    
# Lets see how we can solve the password problem from the assignment using a while loop.
usr = 'Johnny'

for number in range(0, 1000): #Range excludes the last number, like the end term of slices.
    password = str(number)
    while len(password) < 4:
        password = '0' + password
    if usr == 'Johnny' and password == '0001':
        print('Welcome', usr)
        print(password)

# Another case for using a while loop
n = input("Enter a number")
while not n.isnumeric():
    n = input("Enter a number")

print(int(n))

# Recommendation: use 'for loops' when you can know how many times the loop needs
# to be executed or will be executed. If the number of iterations over the loop
# is unknown, the recommeded solution is using a 'while loop'.

###########
# FUNCTIONS
###########

# Area_circle is the name of our function
# radius is the argument that our function takes. We are coercing it t type float.
# we can add other arguments inside these parentheses, separated by commas.
# The declaration of 'float' gives a hint abou the type of input expected by the function.
# The declaration of 'float' AFTER '->' shows the type of output given by the function.
# 
def area_circle(radius: float) -> float :
    # With triple " (double quotation marks) we open the documentation of the function.
    """ This is the text in the documentation of our function.
    Use it to explain what the function does to the user.
    
    Parameters
    ----------
    
    radius: definition of the argument.
    """
    # The next lines are the body of  the function--what it does.
    import math
    sqradius = radius ** 2
    area = math.pi * sqradius
    # Finally, we need to return the output of the function.
    # This is because the functions create their own environment.
    return area

# Another example.
# Let's create our own function
def my_sqrt(n: int):
    import math
    res = math.sqrt(n)
    # Python only returns one value when executing functions.
    # In cases like this, in which we have two variables to return, the system
    # will create a tuple concatenating the different elements to be returned in
    # one single object (the tuple).
    return res, -res

# For setting the types 'tuple', 'list' or 'dychotomic' we need the module *typing*.
from typing import Tuple, List, Dict

def my_sqrt(n: int) -> Tuple[float, float]:
    import math
    res = math.sqrt(n)
    return res, -res

########
# Assert
########

# Operator that will evaluate whether a condition is true. If negative, it will print an error message.    
assert 5 % 2 == 0

# We can set the error message.
assert 5 % 2 == 0, "Not an even number."

# Define a function
def slow_sum(a: int, b: int) -> int:
    """
    Returns the sum of a and b. 
    """
    if a > 0:
        while a > 0:
            a -= 1
            b += 1
    elif a < 0:
        while a < 0:
            a += 1
            b -= 1
    return b

############
# Assignment
############

# Build a function that turns a string over (end to start).
# Like "abcd" => "dcba"

def str_invert(st: str) -> str:
    ist = list(st)
    for i in range(len(st)):
        ist[i - 1] = st[-i]
    for i in range(len(ist)):
        ist[len(ist)-i] = ist[i]
    return(''.join(ist))
str_invert("rebold")

def str_invert(st: str) -> str:
    """Returns inverse string."""
    rev = ''
    for i in range(1, len(st) + 1):
        rev = rev + st[-i]
    return rev

# Another solution from class
def str_invert(st: str) -> str:
    """Returns inverse string."""
    rev = ''
    for i in range(-1, -1, -1):
        rev = rev + st[i]
    return rev

def str_invert(st: str) -> str:
    """Returns inverse string."""
    rev = ''
    while len(st) > 0:
        rev += st[-1]
        st = st[:1]
    return rev

def str_invert(st: str) -> str:
    """Returns inverse string."""
    rev = ''
    for char in st:
        rev = char + rev
    return rev


# Professional solution ;)
def str_invert(st: str) -> str:
    """Returns inverse string."""
    return st[::-1] # This is slicing the string starting from the beginnig
                    # (first empty argument) argument, in steps of minus one (third
                    # argument, declared).










 
