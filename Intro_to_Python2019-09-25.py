#!/usr/bin/env python
# coding: utf-8

# # My first _Jupyter Notebook_ !
# 

# In[ ]:


# Run in python Anaconda Prompt
conda create -n intropython python=3.7 jupyter numpy pandas matplotlib scikit-learn

#activate environment
conda activate intropython

# Run the following code (after the '$' sign)
(intropython)$ jupyter notebook
# Now you should be prompted with the jupyter app in a browser window.

# While on a jupyter notebook can get information on the methods we are prompted with using the shortcut shift + tab.


# # Assignment

# In[ ]:


# Ask the user to input by keyboard the diameter of a circle. Then use this to calculate the corresponding circle area.
# Print the result to screen.

# Solución inicial
diameter = input("Insert a number for the diameter of a circle:")
circle_area = ((float(diameter) / 2) ** 2) * 3.141592

print(circle_area)


# In[ ]:


# One-line solution
print("The area is", ((float(input("Insert a number for the diameter of a circle: "))/2) ** 2) * 3.141592)

