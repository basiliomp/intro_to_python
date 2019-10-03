# -*- coding: utf-8 -*-
"""
Sixth session

Created on Thu Oct  3 18:51:31 2019

@author: Basilio M.P.
"""

#####################
# RECURSIVE FUNCTIONS
#####################

# Imagine you want to create a function that calculates the factor number of another given number.
# This would be the example we will try to redo with recursive functions--i.e. without loops!

def factorial(n: int) -> int:
    if n == 0: #There is a mathemathical demonstration that factor 0 is 1.
        return 1
    res = n
    for i in range(1, n):
        res *= i
    return res

factorial(4)
factorial(0)

# Recursive functions can use themselves in their code:
def factorial(n: int) -> int:
    if n == 0: #There is a mathemathical demonstration that factor 0 is 1.
        return 1
    return n * factorial(n - 1)

factorial(4)

# This works because Python tries to solve 'factorial(4)', but at the end of the code
# it needs to calculate 'factorial(3)', and the problem goes on recursively, until 
# the system looks for 'factorial(0)', in which case the function includes a condition
# that solves the factorial. From there, it goes back answering all the steps waiting 
# for a solution (i.e. 'factorial(1)', 'factorial(2)', 'factorial(3)' and 'factorial(4)').

############
# ASSIGNMETS
############

# Try to solve the following problem, first with loops, and then with recursive functions.
# Build a function that returns the number associated to the number given as argument, 
# considering that number as an index in Fibonacci's sequence.
def fibonacci(n: int) -> int:
    """ Returns the nth number of the Fibonacci's sequence. """
    pass
    
    
###
# Another exercise

employees = [[['Alan', 19, 'uk', 'm'],
              ['Ada', 33, 'uk', 'w'],
              ['Sophie', 38, 'fr', 'w']],
              ['Karl', 29, 'ale', 'm'],
              ['Pitagoras', 'gre', 'm'],
              ['Stanislaw', 25, 'ukr', 'm']]

# The first table-list gathers the names of employees in department A, and the second one department B.
# Extract the following information, using as few lines of code as possible:
    # Average age in each department.
    # Maximum age above all employees.
    # Number of nationalities in the company.
    # Share of women in each department
    # Find what is the most frequent nationality.

###
# Another exercise
    
# Calculate whether this is a magic box (a matrix in which every row, column,
# and main diagonal add up to the same number.)
    # Define a function for that.

box = [[4, 9, 2],
       [3, 5, 7],
       [8, 1, 6]]

from typing import List

def is_magic(matrix: List[List]) -> bool:
    """ Return True if every column, row and main diagonal adds up the same. """
    return matrix

    
    
    
    
    
    
    
    
    
    
    
    