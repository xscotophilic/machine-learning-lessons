#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# adding libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# adding dataset
dataset = pd.read_csv('Data.csv')
# for learning purpose we will use only Annual income and Spending score column
X = dataset.iloc[:, 3:].values

# dealing with missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(X)
X = imputer.transform(X)

# ---------------------------------------------------

# No need to transform variables, as there isn't any categorical data,
# so skip below comments

# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')
# X = np.array(ct.fit_transform(X))

# transforming variable using label encoder
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y = le.fit_transform(y)

# ---------------------------------------------------

# No need to apply 

# No need to split data in test and training dataset as we won't be predicting values

# ---------------------------------------------------

# Using Dendogram to find optimal no of clusters

from scipy.cluster import hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance')
plt.show()

no_of_clusters = 5 # 5 is optimal no of clusters as you can see in graph

# ---------------------------------------------------

# Training the Hierarchical clustering model on dataset

from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc =  hc.fit_predict(X) # 5 is optimal no of clusters as you can see in graph

# ---------------------------------------------------

# Graph for Hierarchical clustering
# Graph will take some time to process so give it some time

colors = ['red', 'blue', 'green', 'cyan', 'magenta']

for i in range(0, no_of_clusters):
    plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s = 20, c = colors[i], label = 'cluster ' + str(i))

plt.title('Clusters of customers')
plt.xlabel('Anual Income (k$)')
plt.ylabel('Spending score (1-100)')
plt.show()