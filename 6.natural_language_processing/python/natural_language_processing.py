#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------
# Adding dataset
dataset = pd.read_csv('data.tsv', delimiter = '\t', quoting = 3) # ignoring " quotes in .tsv file

# ---------------------------------------------------
# Cleaning Texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
# We have 1000 reviews
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split() # splliting words
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)

# ---------------------------------------------------
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
# For first try we run this cell with given line below instead of above line and check how many columns it has
# cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()
# print(len(X[0]))
y = dataset.iloc[:, -1].values

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

# No need to apply scalar
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.fit_transform(X_test)

# ---------------------------------------------------
# Applying Naive Bayes Classification
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()

# training Naive Bayes model
classifier.fit(X_train, y_train)

# ---------------------------------------------------
# Predicting the values
y_pred = classifier.predict(X_test)

# ---------------------------------------------------
# Creating Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
acc_scr = accuracy_score(y_test, y_pred)
# check cm and acc_score
