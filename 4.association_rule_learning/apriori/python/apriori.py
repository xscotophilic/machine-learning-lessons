#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Run any of the following command to install the apyori package:
# pip install apyori (in the terminal)
# !pip install apyori (For Google Colab)

# adding libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------

# adding dataset
dataset = pd.read_csv('data.csv', header = None)

transactions = []

# Because Data.sv have 7501 transactions and 20 Columns
for i in range(0, 7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# ---------------------------------------------------

# Training the Apriori model on the dataset
from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

# ---------------------------------------------------

# Visualising the results

# Displaying the first results coming directly from the output of the apriori function results
results = list(rules)

## Putting the results well organised into a Pandas DataFrame
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))

resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
print('---------------------------------------------------')
print()
## Displaying the results non sorted
print(resultsinDataFrame)
print()
print('---------------------------------------------------')
print()

print('------------------------ Displaying the results sorted by descending lifts ------------------------')
print()

## Displaying the results sorted by descending lifts
print(resultsinDataFrame.nlargest(n = 10, columns = 'Lift'))
print()
print('---------------------------------------------------')
