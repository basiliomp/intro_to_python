# -*- coding: utf-8 -*-
"""
Fourth session

Created on Tue Oct  1 19:00:43 2019

@author: Basilio M.P.
"""

######################
# CONDITIONS
######################

password = input('Enter your password: ')

# We can evaluate sentences and run certains bits of code according to that:
if password == "1234":
    print("Right password.")
if password != "1234":
    print("Wrong password.")

# Another take:
if password == "1234":
    print("Right password.")
else:
    print("Wrong password.")
    
# Elif
# Building a conditionals evalutaion
categ = input('')

if categ == "vegetables":
    print("50%")
elif categ == "proteins":
    print("25%")
elif categ == "carbs":
    print("25%")
else:
    print("No valid answer registered.")
    
# Some tricks for dealing with manual input
newinput = "PassWord   "

# Flattening the input
newinput.lower()
# Removing empty spaces from the input
newinput.strip()
# Combining theses two methods at once
newinput.strip().lower()

############
# Assignment
############

# Determine whether a year is leap.
# Ask for an input number and return "leap year" of "non leap year" according to:
# The year is divisible by 4.
# Except when it is also divisible by 100
# In that case, it will only be a leap year if it is divisible by 400.

year = int(input("Insert a year number"))
leap_years = list()

for year in range(404):
    if year % 4 == 0 and year % 400 == 0:
        leap_years.append(year)
        print("{year} is a leap year.".format(year = year))
    elif year % 4 == 0 and year % 100 == 0:
        print("{year} is NOT a leap year.".format(year = year))
    elif year % 4 == 0:
        leap_years.append(year)
        print("{year} is a leap year.".format(year = year))
    else:
        print("{year} is NOT a leap year.".format(year = year))

len(leap_years)   

# Another solution
leap_years = list()
for year in range(404):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap_years.append(year)
        print("{year} is a leap year.".format(year = year))
    else:
        print("{year} is NOT a leap year.".format(year = year))
len(leap_years)

######################
# LOOPS
######################
radii = [1, 2, 3, 14]
for radius in radii:
    print("Radius equals:", radius)

for radius in radii:
    print("The diameter of the circle is:", radius * 2)
    
# Rewriting the assignment for yesterday using loops.

# Storing the list of lines from the text file in a static variable.
# I do this beacuse everytime you use the method filetext.readline() python discards 
# the current line being read for future iterarions.
with open("my_text_file.txt", "rt") as mytxt:
    listtxt = mytxt.readlines()

mytxt = open("my_text_file.txt", "rt")
mytxt.close()

for line in range(len(listtxt)) :
    myline = listtxt[line]
    #print(myline)
    fields = myline.split(",")
    radius = float(fields[1]) / 2
    area = 3.141592 * radius ** 2
    colour = fields[0]
    # Show sentences like 'The circle of X colour has an area of X units'.
    print("The circle of {colour} colour has an area of {area:.2f} units.".format(
            colour = colour, area = area))

#Another (more elegant) take:
with open("my_text_file.txt", "rt") as f:
    for myline in f.readlines():
        fields = myline.split(",")
        radius = float(fields[1]) / 2
        area = 3.141592 * radius ** 2
        colour = fields[0]
        # Show sentences like 'The circle of X colour has an area of X units'.
        print("The circle of {colour} colour has an area of {area:.2f} units.".format(
                colour = colour, area = area))

############
# Assignment
############
    
# Log in machine
# How to make it work with numbers startig wih 0?
usr = 'Johnny'
for number in range(0, 1000): #Range excludes the last number, like the end term of slices.
    password = str(number)
    if usr == 'Johnny' and password == '0001':
        print('Welcome', usr)
        print(password)

# Answers
for number in range(0, 1000): #Range excludes the last number, like the end term of slices.
    password = str(number)
    password = password.zfill(4)
    if usr == 'Johnny' and password == '0001':
        print('Welcome', usr)
        print(password)

for number in range(0, 1000): #Range excludes the last number, like the end term of slices.
    password = str(number)
    if len(password) == 1:
        password = "000" + password
    elif len(password) == 2:
        password = "00" + password
    elif len(password) == 3:
        password = "0" + password
    if usr == 'Johnny' and password == '0001':
        print('Welcome', usr)
        print(password)
        
for number in range(0, 1000): #Range excludes the last number, like the end term of slices.
    password = str(number)
    if len(password) == 1:
        password = "000" + password
    elif len(password) == 2:
        password = "00" + password
    elif len(password) == 3:
        password = "0" + password
    if usr == 'Johnny' and password == '0001':
        print('Welcome', usr)
        print(password)

# Another way to solve it working with the format of the password.
'{:0>4}'.format(password)

# Another way, with an algorithm
password = '0' * (4 - len(str(password))


        
for number in range(0, 1000): #Range excludes the last number, like the end term of slices.
    password = str(number)
    #
    if usr == 'Johnny' and password == '0001':
        print('Welcome', usr)
        print(password)



# Solving an equation with a loop
for x in range(100):
    if (x + 7) / 2 == 16:
        print(x)

# Another example, working with strings in loops. Remember that strings act like lists.
mystr = "hello there folks!"

for char in mystr:
    print(char)

for n in range(len(mystr)):
    print("The character", mystr[n], "has index", n)

############
# Assignment
############

# How many pigs and chicken are in a farm?
    # Let's suppose we know there are 22 heads and 50 legs.
    # In other words:
    # pigs + chicken == 22
    # 4 * pigs + 2 * chicken == 50

# Example of a nested loops
    for pigs in range(3):
        for chicken in range(5):
            print(pigs, chicken)

# Applied to this farm problem:
for pigs in range(23):
    for chicken in range(23):
        if (4 * pigs) + (2 * chicken) == 50 and pigs + chicken == 22:
            print("There are", pigs, "pigs and ", chicken, "chicken")

# A more efficient way to solve the equations system
for pigs in range(23):
    chicken = 22 - pigs
    if (4 * pigs) + (2 * chicken) == 50 and pigs + chicken == 22:
        print("There are", pigs, "pigs and ", chicken, "chicken")
        