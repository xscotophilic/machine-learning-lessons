#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# adding libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# adding dataset
dataset = pd.read_csv('data.csv')
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

# No need to apply scalar
# No need to split data in test and training dataset as we won't be predicting values

# ---------------------------------------------------

# Using Elbow method to find optimal no of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS (Within-Cluster-Sum-of-Squares)')
plt.show()

no_of_clusters = 5 # 5 is optimal no of clusters as you can see in graph

# ---------------------------------------------------

# Training the k means model on dataset
# 5 is optimal no of clusters as you can see in graph
kmeans = KMeans(n_clusters = no_of_clusters, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(X)

# ---------------------------------------------------
# Graph for K means clustering
# Graph will take some time to process so give it some time

colors = ['red', 'blue', 'green', 'cyan', 'magenta']

for i in range(0, no_of_clusters):
    plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s = 20, c = colors[i], label = 'cluster ' + str(i))

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'centroids')
plt.title('Clusters of customers')
plt.xlabel('Anual Income (k$)')
plt.ylabel('Spending score (1-100)')
plt.show()