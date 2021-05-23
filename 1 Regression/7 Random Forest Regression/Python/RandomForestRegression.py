#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# adding dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# adding dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# transforming y into 2d
y = y.reshape(len(y), 1)

# dealing with missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(X)
X = imputer.transform(X)

# transforming an independent variable
# here 1st column is already encoded and represented as column 2 in csv file
# so we will use only 2nd column as an independent variable and won't transform it

# splitting data in test and training dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 400)

# Applying scalar
# scalar expects 2d array
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
y_train = sc_y.fit_transform(y_train)
y_test = sc_y.transform(y_test)

# ---------------------------------------------------
# Applying Random Forest Regressor
# RandomForestRegressor expects 1d array
y_train = y_train.reshape(-1)
y_test = y_test.reshape(-1)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state=0)
regressor.fit(X_train, y_train)

# ---------------------------------------------------
# Predicting the values
y_pred = sc_y.inverse_transform(regressor.predict(X_test))

# ---------------------------------------------------
# Graph for Decision Tree Regression
# RED DOTS REPRESENTS THE TEST PREDICTIONS
# GREEN DOTS REPRESENTS THE TRAIN SET ACTUAL VALUES
# BLUE DOTS REPRESENTS THE REGRESSION LINE

# smoothing the curve
X_train_grid = np.arange(min(X_train), max(X_train), 0.1)
X_train_grid = X_train_grid.reshape(len(X_train_grid), 1)

plt.scatter(sc_X.inverse_transform(X_train), sc_y.inverse_transform(y_train), color = 'green')
plt.scatter(sc_X.inverse_transform(X_test), y_pred, color = 'red')
plt.plot(sc_X.inverse_transform(X_train_grid), sc_y.inverse_transform(regressor.predict(X_train_grid)), color = 'blue')
plt.title('Position vs Salary (Decision Tree Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()# BLUE DOTS REPRESENTS THE REGRESSION LINE