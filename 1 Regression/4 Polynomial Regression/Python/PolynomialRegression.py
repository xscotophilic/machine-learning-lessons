#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# adding libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# adding dataset
dataset = pd.read_csv('Data.csv')

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
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = None, shuffle=False, stratify=None)

# ---------------------------------------------------
# Applying simple linear regression
from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(X_train, y_train)

# ---------------------------------------------------
# Graph for linear regressor
# RED DOTS REPRESENTS THE TEST PREDICTIONS
# GREEN DOTS REPRESENTS THE TRAIN SET ACTUAL VALUES
# BLUE DOTS REPRESENTS THE REGRESSION LINE
plt.scatter(X_train, y_train, color = 'green')
plt.plot(X_test, linear_regressor.predict(X_test), color = 'red')
plt.plot(X_train, linear_regressor.predict(X_train), color = 'blue')
plt.title('Position vs Salary (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# ---------------------------------------------------
# Applying polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X_train)
X_poly_test = poly_reg.fit_transform(X_test)
linear_reg_forpoly = LinearRegression()
linear_reg_forpoly.fit(X_poly, y_train)

# ---------------------------------------------------
# Graph for polynomial regressor 
# RED DOTS REPRESENTS THE TEST PREDICTIONS
# GREEN DOTS REPRESENTS THE TRAIN SET ACTUAL VALUES
# BLUE DOTS REPRESENTS THE REGRESSION LINE
plt.scatter(X_train, y_train, color = 'green')
plt.scatter(X_test, linear_reg_forpoly.predict(X_poly_test), color = 'red')
plt.plot(X_train, linear_reg_forpoly.predict(X_poly), color = 'blue')
plt.title('Position vs Salary (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()