# -*- coding: utf-8 -*-
"""
Eight session

Created on Tue Oct  8 18:09:15 2019

@author: Basilio
"""

#################
# Class exercises
#################

# Exercise A
# Calculate a summatory for all numbers between 1 and 100.
def summation(n:int) -> int:
    assert n >= 0, "Insert a positive number."
    summ = 0
    for i in range(n + 1):
        summ += i
    return summ
    
summation(100)

# Calculate a summatory for all EVEN numbers between 1 and 100
def even_summ(n:int) -> int:
    assert n >= 0, "Insert a positive number."
    summ = 0
    for i in range(n + 1):
        if i % 2 == 0:
            summ += i
    return summ
        
even_summ(100)

# How many of the numbers between 0 and 100 are divisible by 13.

def thirteen_div(n:int) -> int:
    assert n > 0, "Insert a positive number."
    count_div = 0
    if n == 0:
        return 1
    for i in range(1, n + 1):
        if i % 13 == 0:
            count_div += 1
    return count_div
        
thirteen_div(100) # There are 7 numbers divisible by 13 in the range 0-100.

# Exercise B: Markov chains
# Given a sequence of (apparently) random numbers in the range 0-9,
# build a matrix storing the number of appereances for each couple of
# numbers (i.e. [my_sequence[0], my_sequence[1]] ) in steps of one (so each
# number will be used twice, first as the initial element, then as the final one).
# The way to store the number of appereances for each couple of digits is in a
# matrix 10x10, in wich the initial digit in the two-digits subset points to the
# row, and the second digit to the column.

# In other words, if the sequence of (apparently) random numbers starts with 
# [4, 1, 0, 9, ...] we should first count one appearence for the row 4, column 1,
# then another for row 1, column 0, and so on.
from typing import List

# In case the list of random numbers were given in a string
seq = "957230958701397510394751396285730298609267069026250967"
seq_int = []
for num in seq:
    seq_int.append(int(num))

def markov(seq:List[int], matrix_size:int) -> List[List[int]]:
    # Defining the empty matrix for storing results
    markov_matrix = []
    
    # Extending the empty matrix to store as columns as necessary.
    for i in range(0, matrix_size):
        markov_matrix.append([0] * matrix_size)
    
    # Creating the set of two-digits list that will form the Markov chain.
    for i in range(len(seq) - 1):
        chain_link = [seq[i], seq[i + 1]]
        markov_matrix[chain_link[0]][chain_link[1]] += 1
    
    return markov_matrix

# Testing
markov(seq_int, 10)
mkmx = markov(seq_int, 10)

########### WORK IN PROGRESS FROM NOW ON

# Variance across rows and colums
for i in range(len(mkmx)):
    mean_row = sum(mkmx[i]) / len(mkmx)
    print(mean_row)

for n in range(len(mkmx)):
    for i in range(len(mkmx[n])):
            summ_age += mkmx[n][i]
            [] summ_age / len(mkmx[n])
# Include a calculation of the standard deviation acrosss the matrix.

###########

#############
# Assignments
#############
            
# Build a function to test whether a number in prime.
def is_prime(n:int) -> bool:
    """ Evaluates whether the number given is prime. """
    if n <= 0:
            return False
    elif n == 1:
            return True
    for i in range(1, n):
        if n % i == 0:
            return False
    return True

# Build a function that calculates the slope and intercept parameters in
# a linear regression.

from typing import List, Dict

xvec = [0, 1, 2, 3, 4, 5, 6, 7]
yvec = [0, -1, -2, -3, -4, -5, -6, -7]

def lin_reg(xvec:List, yvec:List) -> Dict:
    import math
    n = len(xvec)
    b_0 = 0
    b_1 = 0
    sqr_xvec = []
    sqr_yvec = []
    xtimesy = []
    # Calculate necessary parameters
    for i in range(len(xvec)):
        sqr_xvec.append(xvec[i] ** 2)
        #print(sqr_xvec)
        sqr_yvec.append(yvec[i] ** 2)
        #print(sqr_xvec)
        xtimesy.append(xvec[i] * yvec[i])
        #print(sqr_xvec)
    # Solving beta zero
    
    for i in range(len(xvec)):
        
    #(sum(xvec) * sum(yvec) - n * sum(xtimesy)) / sum(xvec) ** 2
    #b_1 = (n * sum(xtimesy)) - (sum(xvec) * sum(yvec)) / (n * sum(sqr_xvec)) - (sum(xvec) ** 2)
    b_0 = sum(yvec) - b_1 * sum(xvec) / n    
    # Building the output
    #lin_reg = {"intercept": b_0 ,
    #                  "slope": b_1}
    lin_reg = [b_0, b_1]   
    return lin_reg
        
lin_reg(xvec, yvec)   
        
        
        
        


mpg = [21,
21,
22.8,
21.4,
18.7,
18.1,
14.3,
24.4,
22.8,
19.2,
17.8,
16.4,
17.3,
15.2,
10.4,
10.4,
14.7,
32.4,
30.4,
33.9,
21.5,
15.5,
15.2,
13.3,
19.2,
27.3,
26,
30.4,
15.8,
19.7,
15,
21.4]

hp = [110,
110,
93,
110,
175,
105,
245,
62,
95,
123,
123,
180,
180,
180,
205,
215,
230,
66,
52,
65,
97,
150,
150,
245,
175,
66,
91,
113,
264,
175,
335,
109,
]

lin_reg(mpg, hp)













            
            
