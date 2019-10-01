# -*- coding: utf-8 -*-
"""
Fourth session

Created on Tue Oct  1 19:00:43 2019

@author: Basilio
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
# Except when it is also ... 100
# 400


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
    
# Log in machine
# How to make it work with numbers startig wih 0?
usr = 'Johnny'
for number in range(0, 1000): #Range excludes the last number, like the end term of slices.
    password = str(number)
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

# How many pigs and chicken are in a farm?
    # Let's suppose we know there are 22 heads and 50 legs.
    # In other words:
    pigs + chicken == 22
    4 * pigs + 2 * chicken == 50

# Nested loops
    for n in range(3):
        for m in range(5):
            print(n, m)

# Applied to this farm problem:
for n in range(23):
    for m in range(51):
        if (4 * n) + (2 * n) == m and n + m == 22 and m == 50:
            print(n, m)





















