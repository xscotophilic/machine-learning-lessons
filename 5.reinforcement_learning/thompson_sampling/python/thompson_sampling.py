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

# Implementation of Thompson Sampling

import random

N = 10000 # as you can see dataset has 10,000 users (rows)
d = 10 # no of ads in dataset
ads_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
total_reward = 0

for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if (random_beta > max_random):
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        numbers_of_rewards_1[ad] += 1
    else:
        numbers_of_rewards_0[ad] += 1
    total_reward += reward

# ---------------------------------------------------

# Visualising the results
plt.hist(ads_selected)
plt.title('')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()