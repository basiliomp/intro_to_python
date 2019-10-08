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

# Iterative solution
def fibonacci(n: int) -> int:
    """ Returns the nth number of the Fibonacci's sequence. """
    assert n >= 0, "Bad input"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c
    
# Recursive solution
def fibonacci(n: int) -> int:
    """ Returns the nth number of the Fibonacci's sequence. """
    assert n >= 0, "Bad input"
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
# In this example, the recursive function is much slower!
# Try it by calling each of these functions with a large number as argument.
    
###
# Another exercise

employees = [[['Alan',  19, 'uk', 'm'],
              ['Ada',   33, 'uk', 'w'],
              ['Sophie',38, 'fr', 'w']],
             [['Karl',  29, 'ale', 'm'],
              ['Pitagoras', 49, 'gre', 'm'],
              ['Stanislaw', 25, 'ukr', 'm']]]

# The first table-list gathers the names of employees in department A, and the 
# second one department B.
# Extract the following information:
    
    # Average age in each department.
def avg_dept(n: int) -> float:
    summ_age = 0
    for i in range(len(employees[n])):
        summ_age += employees[n][i][1]
    return summ_age / len(employees[n])
    
    # Maximum age above all employees.
from typing import List
def max_age(employees: List[List[List]]) -> int:
    maximum = 0
    for dept in employees:
        for person in dept:
            if person[1] > maximum:
                maximum = person[1]
    return maximum
    
    # Number of nationalities in the company.


    # Share of women in each department
def share_women(dept: List[List]) -> float:
    n_women = 0
    for person in dept:
         if person[3] == 'w':
             n_women += 1
    return (n_women / len(dept)) * 100

    # Find what is the most frequent nationality.
def freq_nation(employees: List[List[List]]) -> int:
    nationalities = list()
    for dept in employees:
        for person in dept:
            nationalities.append(person[2])
    nation.mode = 'none'
    for nation in nationalities:
        if nationalities.count(nationalities[nation]) > nation.mode:
            nationalities.insert(0, nationalities[nation])
    return nationalities


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
    
    #Checking if there are as many rows as columns.
    assert len(matrix) == len(matrix[0]), 'Matrix is not squared.'
    dimension = len(matrix) # Once we know it is a squared matrix.
    magic_sum = sum(matrix[0]) # All the other possible sums should equal this value.
        
    # Checking the rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    for id_col in range(dimension): # Id_col will be 0, then 1, then 2 in this case.
        col_sum = 0
        for row in matrix:
            col_sum += row[id_col]
        if col_sum != magic_sum:
            return False
    
    # Checking the cloumns
    for id_col:
    
    # Checking the main diagonal
    sum_diag = 0
    for index in range(dimension):
        # Row and columns indexes must be equal for the numbers in the main digaonal.
        sum_diag += matrix[index][index]
    if sum_diag != magic_sum:
        return False
    
    # Checking the secondary diagonal
    sum_diag = 0
    for index in range(dimension):
        # Row and columns indexes must be equal for the numbers in the main digaonal.
        sum_diag += matrix[index][dimension - 1 - index]
    if sum_diag != magic_sum:
        return False
    
    return True
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    