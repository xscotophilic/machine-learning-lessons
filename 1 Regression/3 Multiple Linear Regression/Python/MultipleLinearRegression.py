#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Adding libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Adding Dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Taking care of missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer( missing_values = np.nan, strategy='mean')
imputer.fit(X[:, 0:3])
X[:, 0:3] = imputer.transform(X[:, 0:3])

# Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# Applying encoding to column no 4 because 4th column has categorical data
# (But we have to put 3 because index starts from 0)
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [3])], remainder = 'passthrough')
X = np.array(ct.fit_transform(X))

# Dividing data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)

# Trainng the Multiple linear regression model (optimal model selected automatically by sklearn) on training dataset
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting the test set result
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)

# For printing directly use print(y_pred, '\n\, y_test)

# For printing values side by side for comparing use below code
# First is predicted column and second is real value column
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))