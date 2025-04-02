#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------

# adding dataset
dataset = pd.read_csv('data.csv')

# ---------------------------------------------------

# Implementation of Upper Confidence Bound(UCB)

import math

N = 10000 # as you can see dataset has 10,000 users (rows)
d = 10 # no of ads in dataset
ads_selected = []
sums_of_rewards = [0] * d # sums_of_rewards = sum of rewards when (a) taken prior to (t)
numbers_of_selections = [0] * d # numbers_of_selections = no. of times (a) taken prior to (t)
total_reward = 0

for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if numbers_of_selections[i] > 0 :
            average_reward = sums_of_rewards[i]/numbers_of_selections[i]
            delta_i = math.sqrt(((3/2)* math.log(n+1))/numbers_of_selections[i]) # because log(0) = infinity and N can be zero by our given loop
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if (upper_bound > max_upper_bound):
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] += 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] += reward
    total_reward += reward

# First 10 rounds will select all 10 ads and after that we use given algorithm to select ads

# ---------------------------------------------------

# Visualising the results
plt.hist(ads_selected)
plt.title('')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()