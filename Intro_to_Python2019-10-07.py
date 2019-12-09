# -*- coding: utf-8 -*-
"""
Seventh session

Created on Mon Oct  7 19:33:20 2019

@author: Basilio
"""
###################
# Mathematical sets
###################
# A set is a collection of unique objects
s = set()
print(len(s))

# Adding the first element into the set 's'
s.add('b')
print(len(s))
print(s)

# Sets do not admit duplicates.
# Adding a second (different) element
s.add('a')
print(len(s))
print(s)

# Adding a third (already present!) element
s.add('b')
print(len(s))
print(s)

# Sets are unordered.
for element in set([1, 5, 9, 2]):
    print(element)

################
# More on lists.
################
    
# Imagine you are storing values in an empty
l = []
for i in range(3):
    l.append(i)
print(l)

# That would be totally equivalent to:
l = [i for i in range(3)]
print(l)
