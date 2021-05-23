#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# adding libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# adding dataset
dataset = pd.read_csv('Data.csv')

# splitting a dataset into independent and dependent variables
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# dealing with missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(X)
X = imputer.transform(X)

# ---------------------------------------------------
# No need to transform independent variables, as there isn't any categorical data,
# so skip below comments

# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')
# X = np.array(ct.fit_transform(X))

# No need to transform dependent variable, as dependent variable already have 0 or 1 value,
# so skip below comments

# transforming a dependent variable
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y = le.fit_transform(y)
# ---------------------------------------------------

# Splitting data in test and training dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 404)

# Applying scalar
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

