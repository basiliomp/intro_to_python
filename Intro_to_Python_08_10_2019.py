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
    for i in range(1, n):
        if n <= 0:
            return False
        elif n % i == 0 and and i != 1 and i != n:
            print(i, n)
            return False
    return True

# Build a function that calculates the 























            
            
