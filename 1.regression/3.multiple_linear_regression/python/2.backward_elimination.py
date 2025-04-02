#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Adding libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Adding Dataset
dataset = pd.read_csv('data.csv')
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 1)

# Trainng the Multiple linear regression BACKWARD ELIMINATION model on training dataset
import statsmodels.api as sm
# Adding intercept (adding first column of constant 1)
X = np.append(arr = X, values = np.ones((50, 1)).astype(int), axis=1 )

X_opt = np.array(X[:, [0, 1, 2, 3, 4, 5]], dtype=float)
#OrdinaryLeastSquares
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())

# remove column for which p>alpha(0.05)
X_opt = np.array(X[:, [0, 1, 2, 3, 5]], dtype=float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())

# remove column for which p>alpha(0.05)
X_opt = np.array(X[:, [0, 1, 2, 3]], dtype=float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())

# remove column for which p>alpha,
# but here no such column found so we get our model
