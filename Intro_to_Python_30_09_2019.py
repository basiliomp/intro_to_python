# -*- coding: utf-8 -*-
"""
Third session

Created on Mon Sep 30 19:05:14 2019

@author: Basilio
"""

###########################
# Assigning with operations
###########################

n_times = 1
print(n_times)

n_times += 1
print(n_times)

n_times += 1
print(n_times)

# We are reassigning the value to the variable 'n_times' at the same time we are
# modifying / updating its value.

# This works with other mathematical operators too.
n_times -= 0.5
print(n_times)

n_times *= 2
n_times %= 2

########################
# More numeric functions
########################

2 ** 10 == pow(2, 10)

min()
max()
sum()

# It is possible to get a lot more mathematical functions activating the library math
# Importing libraries
import math

# Square root
math.sqrt(64)
# Rounding to the upper nuber; its ceiling.
math.ceil(5.5)
# Rounding to the lower nuber; its floor.
math.floor(5.5)
# It stores special nummbers as well.
math.pi
math.e

#########
# Strings
#########

mystr = 'abc'

# Strings can be sliced as lists
mystr[0:2]

# Strings has their own methods, which can be invoked with a dot after the string name
mystr.isnumeric()
mystr.isnumeric()
mystr.endswith('c')
'silly string'.endswith('c')

names = "Alan, Jordi, Sophie, Karol"
len(names)
names.split(',')
len(names.split(','))

# The plus symbol concatenates strings
'Alan' + ' ' + 'Turing'

print('###' * 4)
      
############################
# Print and format functions
############################
result = 99
error = 66
print('Result equals ' + str(result) + ' and the error is ' + str(error) + '.')

# Another way to print strings invoking numeric variables
# The symbol % indicates that we are invoking a variable, the 'f' after it states
# that we are invoking a float variable, and the number after it (in this example, 1)
# indicates the number of decimals to be printed. '%d' indicates a integer number.

'Result equals %.1f and the error is %d' % (result, error)

'Result equals {:.1f} and the error is {}'.format(result, error)

'Result equals {res:.1f} and the error is {err} for the result {res}'.format(
        res = result, err = error)

###########
# Files
###########

# Let us create a variable pointing to our newly created 'new_text_file.txt'
# For reading a text file, the second argument of the open function should be r.
# Conversely, use the argument w for writing.

# Modes for the function 'open()'
#   Read (r), Write (w)
#   TExt (t), Binary (b)

f = open('new_text_file.txt', 'rt')

type(f)

# The metho .readline() prints one line each time, advancing through the document in
# following uses.
# EOF is an abbreviation for End of File.
f.readline()
f.readline()
# Python will keep the position in which we are in a text. Run the code below to see it.
f.readline()

# Always close your documents after reading or writing.
f.close()

# Another option is to read the whole document in one shot.
f = open('new_text_file.txt', 'rt')
f.readlines()

#After that, we reach End Of File and nothing new will be printed.
f.readlines()
f.readline()
# Always close your documents after reading or writing.
f.close()

# Creating a new text file and writing in it.
f = open('another_file.txt', 'wt')
f.write('This is the first line of my second text file. \n')
f.write('And thi is the second line of my second text file. \n')
f.close()

# Writing the first text file adding new lines!
f = open('new_text_file.txt', 'at')
f.write('This is another line of my first text file. \n')
f.close()

f = open('new_text_file.txt', 'rt')
f.readlines()

# Scopes
# Tabulation allows us to work within a scope, a set of instructions in order that 
# will run some other code at its end.

# For example, 'with open()' will close (as in f.close()) the file at the end of the scope.
with open('new_text_file.txt', 'rt') as fil:
    print(fil.readlines())
# Since here there is no tabulation at the star of the line, we are out of the scope
print('I\'m out!')

print(fil.readlines())

###################
# Logical operators
###################

2 < 3
3 > 0
2 ** 10 == 1024
not (2 ** 10 == 1024)
7 > 3 and 10 > 5
3 != 5
3 != 5 or 0 == 1

# Hierarchy of logical evaluations:
# 1st: and statements
# 2nd: or statements
# 3rd: not statements

7 > 4 and 7 <= 10 and 7 != 5 and 6 >= 8 or 9 < 12

### if statements
tweet = 'The product I purchased is broken!'

# The operator 'in' searches in strings whether the first one is present in the second one.
'broken' in tweet

if 'broken' in tweet:
    print('Warning! Negative message detected.')

company_name = 'Company\'s ltd.'
if 'broken' in tweet and company_name in tweet:
    print('Warning! Negative message about your company detected.')

tweet2 = 'The product I purchased from Company\'s ltd. is broken!'
if 'broken' in tweet2 and company_name in tweet2:
    print('Warning! Negative message about *your company* detected.')
#
    
############
# Assignment
############

### First exercise 
    
    # Copy instructions from BaseCamp
    
    # Create a text file in which each line contains a colour and a number (diameter).
    mytxt = open("my_text_file.txt", "wt")
        
    import os 
    os.listdir()
    
    mytxt.write('red, 8 \n')
    mytxt.write('blue, 3 \n')
    mytxt.write('green, 9.2 \n')
    mytxt.write('yellow, 3.1 \n') 
    mytxt.write('orange, 5 \n')
    mytxt.write('black, 0.66')
    
    mytxt.close()
    # Read it
    mytxt = open("my_text_file.txt", "rt")
    mytxt.readlines()
    # Show sentences like 'The circle of X colour has an area of X units'.
print("The circle of %s colour has an area of %s units.")

### Second exercise 
    
    # Read a text file with keywords, one for each line (assuming you know how many there are).
    
    # Show a warning when a sentence with one of those keywords is written in the keyboard input.
    
    # Write those sentences with keywords in a new file.



















