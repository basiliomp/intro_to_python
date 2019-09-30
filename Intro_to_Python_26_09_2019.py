#!/usr/bin/env python
# coding: utf-8

# # Second class
# 

# In[ ]:


# Run in python Anaconda Prompt
conda create -n intropython python=3.7 jupyter numpy pandas matplotlib scikit-learn

#activate environment
conda activate intropython

# Run the following code (after the '$' sign)
### (intropython)$ jupyter notebook
# Now you should be prompted with the jupyter app in a browser window.


# In[18]:


# Create a list, wich is a conjunction of elemtents. Those elements may be of different types.
heterogeneous_list = [1, True, "three", 4]

# We can subset elements from the list using square braquets [] 
# Python starts counting at 0: the first index position is 0, the second one is 1, and so on.
# We can call a position in reverse order (starting from the end of the list)
heterogeneous_list[-1]


# In[19]:


# Add elements to the list heterogénea
heterogeneous_list.append("five")
print(heterogeneous_list)

# Here we are using for the first time a method. That is, the ".append" included at the end of our object's name.
# Python is an object-oriented language. This implies that there are certain types of commands, called methods, 
# wich can be applied to objets. Methods are a set of operations that can be applied over objects.


# In[20]:


# More on slicing
# list[start : end : step]
heterogeneous_list[2::2]


# In[ ]:


# A list is a mutable concatenation of objects, with no constrains on the type of information stored.


# In[25]:


# Matrixes
matrix = [[1 , 2], [3, 4]]
matrix[0]


# In[24]:


# Slicing within matrixes
matrix[0][0]


# In[4]:


# Difference between the method .append() and the method .extend()
l0 = [1, 2, 3]
l1 = ['a', 'b', 'c']

l0.append(l1)
print(l0)

l


# In[8]:


# Tuples
# An immutable list is of objects, with no constrains on the type of information stored.

mytuple = (1, True, "three", 4)
type(mytuple)

# Since tuples are immutable, trying to rewrite, delete of modify its elements will raise an error.
mytuple[3] = 3


# In[ ]:


# As we did with lists, tuples also have methods assigned. We can use them writing a 
# dot and the name of the method after the name of the tuple.

# Use 'tab' after the dot to get a hint of the methods available for the type of object in use.
mytuple.count()
mytuple.index()

# Slicing works the same way in tuples and lists.
mytuple[0]
mytuple[0::3]


# # Assignment
# 
# Build the following matrix:
# $$\begin{pmatrix}
# 3 & 4 & 7 & 2 \\
# 1 & 0 & 1 & 1 \\
# 5 & 6 & 3 & 10
# \end{pmatrix}$$
# 
mymatrix = [[3, 4, 7, 2],
            [1, 0, 1, 1],
            [5, 6 ,3 ,10]]
print(mymatrix)

# Mean of each row
current_r = 0
sum(mymatrix[current_r]) / len(mymatrix[current_r])

current_r = 1
sum(mymatrix[current_r]) / len(mymatrix[current_r])

current_r = 2
sum(mymatrix[current_r]) / len(mymatrix[current_r])

# Mean of each column
current_c = 0
(mymatrix[0][current_c] + mymatrix[1][current_c] + mymatrix[2][current_c]) / 3

current_c = 1
(mymatrix[0][current_c] + mymatrix[1][current_c] + mymatrix[2][current_c]) / 3

current_c = 2
(mymatrix[0][current_c] + mymatrix[1][current_c] + mymatrix[2][current_c]) / 3

current_c = 3
(mymatrix[0][current_c] + mymatrix[1][current_c] + mymatrix[2][current_c]) / 3

# Number of elements in the matrix.
len(mymatrix[0]) + len(mymatrix[1]) + len(mymatrix[2])
    # Alternative (actually better!) solution
    len(mymatrix) * len(mymatrix[0])

# Sum of all the elements ins the matrix.
sum(mymatrix[0] + mymatrix[1] + mymatrix[2])

# Minimum value in the matrix.
min(min(mymatrix))

# Maximum value in the matrix.
max(max(mymatrix))

# Mean of all elements in the matrix.
sum(mymatrix[0] + mymatrix[1] + mymatrix[2]) / (len(mymatrix) * len(mymatrix[0]))
