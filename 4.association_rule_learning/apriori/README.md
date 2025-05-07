# Apriori Algorithm

> **Apriori Property:** All non-empty subsets of a frequent itemset must also be frequent.

## Table of Contents
- [Overview](#overview)
- [Algorithm Steps](#algorithm-steps)
- [Visualization](#visualization)
- [Further Reading](#further-reading)

## Overview
The Apriori algorithm is a classic algorithm used in data mining for learning association rules. It is especially useful for market basket analysis, where the goal is to find associations between items purchased together.

## Algorithm Steps
1. **Set minimum support and confidence.**
2. **Find all itemsets in transactions** with support higher than the minimum support.
3. **Generate association rules** from these itemsets with confidence higher than the minimum confidence.
4. **Generate candidate itemsets** by joining frequent itemsets from the previous iteration.
5. **Prune candidates** that contain infrequent subsets or do not satisfy minimum support.
6. **Repeat** steps 4 and 5 until no further itemsets can be generated.

**Mathematical Intuition:**
- Uses the Apriori property: all non-empty subsets of a frequent itemset must also be frequent.
- Iteratively builds larger itemsets from smaller ones, pruning those that do not meet minimum support.

## Visualization

![Apriori Algorithm Example](readme_assets/Apriori_algorithm_example.png)

## Further Reading
- [Apriori: Association Rule Mining In-depth Explanation and Python Implementation – Towards Data Science](https://towardsdatascience.com/apriori-association-rule-mining-explanation-and-python-implementation-290b42afdfc6)
- [Apriori Algorithm – GeeksforGeeks](https://www.geeksforgeeks.org/apriori-algorithm/)
