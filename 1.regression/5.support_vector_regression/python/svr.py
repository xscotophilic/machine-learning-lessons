#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# adding libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# adding dataset
dataset = pd.read_csv('data.csv')

# splitting a dataset into independent and dependent variables
# here 1st column is already encoded and represented as column 2 in csv file
# so we will use only 2nd column as an independent variable
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# No need to deal with missing values
# as csv file doesn't contain any column which can have missing values

# No need to transform any independent variable
# as we will be using 2nd column (which is numerical) to train and test model.

# splitting a dataset into training and test
# We have only 10 rows as data so we will not split dataset

# ---------------------------------------------------
# Applying Feature Scalling

# transforming y into 2d
y = y.reshape(len(y), 1)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# ---------------------------------------------------
# Applying SVR
# RBF kernel = Radial basis function kernel
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

X_pred = [[6.5]]
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(X_pred)))

# ---------------------------------------------------
# Graph for SVR
# RED DOTS REPRESENTS THE TEST PREDICTIONS
# GREEN DOTS REPRESENTS THE TRAIN SET ACTUAL VALUES
# BLUE DOTS REPRESENTS THE REGRESSION LINE
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'green')
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(regressor.predict(X)), color = 'blue')
plt.title('Position vs Salary (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()