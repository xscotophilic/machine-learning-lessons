#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# *************************************************************************************
# ** Part 1 Data processing
# *************************************************************************************

# Importing the libraries
import numpy as np
import pandas as pd
import tensorflow as tf

# ---------------------------------------------------
# Adding dataset
dataset = pd.read_csv('data.csv')

# splitting a dataset into independent and dependent variables
X = dataset.iloc[:, 3:-1].values # excluding all the columns which have no impact on outcome/ dependent variable
y = dataset.iloc[:, -1].values

# No need to deal with missing values (as per given dataset)
# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
# imputer.fit(X)
# X = imputer.transform(X)

# ---------------------------------------------------
# transforming an independent variable (i.e. Gender), which only contains binary value (i.e. male and female in dataset)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])

# Transforming independent variables (i.e. Geography), as there isn't any relation between given values (i.e. France, Spain, Germany)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [1])], remainder = 'passthrough')
X = np.array(ct.fit_transform(X))

# ---------------------------------------------------
# Splitting data in test and training dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 404)

# # Applying scalar
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# *************************************************************************************
# ** Part 2 Building the ANN
# *************************************************************************************

# ---------------------------------------------------
# Initializing the ANN
ann = tf.keras.models.Sequential()

# ---------------------------------------------------
# Adding the input layer and first hidden layer
ann.add(tf.keras.layers.Dense(units = 6, activation = 'relu'))

# ---------------------------------------------------
# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units = 6, activation = 'relu'))

# ---------------------------------------------------
# Adding the output layer
ann.add(tf.keras.layers.Dense(units = 1, activation = 'sigmoid'))

# *************************************************************************************
# ** Part 3 Training the ANN
# *************************************************************************************

# ---------------------------------------------------
# Compiling the ANN
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# ---------------------------------------------------
# Training the ANN on the training set
ann.fit(X_train, y_train, batch_size = 32, epochs = 100)

# *************************************************************************************
# ** Part 4 Making the predictions and evaluating the model
# *************************************************************************************

# ---------------------------------------------------
# Predicting the values
y_pred = ann.predict(X_test)
y_pred = y_pred > 0.5

# ---------------------------------------------------
# Creating Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
acc_scr = accuracy_score(y_test, y_pred)
