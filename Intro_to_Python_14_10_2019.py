# -*- coding: utf-8 -*-
"""
Eleventh session

Created on Mon Oct 14 17:17:35 2019

@author: Basilio M.P.
"""

############################
# NumPy, MatPlotLib, Seaborn
############################
print(new_var)
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

# Our own linear regression
true_a = 2
true_b = 5

xs = [x for x in range(200)]
ys = []
for x in xs:
    ys.append(true_a * x + true_b + np.random.normal(0, (x / 10) ** 1.5))

fig, ax = plt.subplots()
ax.scatter(xs, ys)

x_mean = sum(xs) / len(xs)
y_mean = sum(ys) / len(ys)

num = 0
for x, y in zip(xs, ys):
    num += (x - x_mean) * (y - y_mean)
den = 0
for x in xs:
    den += (x - x_mean) ** 2

# Solving a, the slope of the linear regression
a = num / den
print(a)

# Solving b, the intercept of the linear regression
b = y_mean - a * x_mean
print(b)

# Graphical representation of the linear regression
fig, ax = plt.subplots()
ax.scatter(xs, ys)
ax.plot([0, 200], [a * 0 + b, a * 200 + b], 'r', lw=5, alpha=.7)

# Another library for graphical representation: bokeh
# And there is also plotly, especially a food option for 3-d graphics.
