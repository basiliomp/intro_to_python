# -*- coding: utf-8 -*-
"""
Eleventh session

Created on Mon Oct 14 17:17:35 2019

@author: Basilio M.P.
"""

############################
# NumPy, MatPlotLib, Seaborn
############################

import numpy as np

# Methods available in numpy: dozens!
# It is better to use numpy when possible because it is more efficient than base Python.

np.zeros((10, 1), dtype = int) # First argument is a tuple indicating rows and columns.

from matplotlib import pyplot as plt

distr = np.random.poisson(0, size = 200)
fig, ax = plt.subplots()
ax.hist(distr, bins = 100)

conda install seaborn

import seaborn as sns

matrix = np.random((10, 10))

sns.heatmap(matrix)

conda install scikit-learn

from sklearn.linear_model import LinearRegression

LinearRegression(xvec, yvec)

model = LinearRegression()
model.fit(xvec.reshape(-1, 1), yvec.reshape(-1, 1))
model.coef_
model.intercept_
model.predict([[100]])
type(model)
