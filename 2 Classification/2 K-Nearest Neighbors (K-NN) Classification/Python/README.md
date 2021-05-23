# Solve K Nearest Neighbor (KNN) Classification in Python
> This program preprocesses the data and applies K Nearest Neighbor (KNN) Classification.

*  K Nearest Neighbor (KNN) Classification is an algorithm for classification used to assign a discrete set of classes to observations. Email spam or not spam, fraud or not fraud are some of the examples of classification problems.

* The KNN algorithm assumes that similar things exist in close proximity. In other words, similar things are near to each other.

<img src="KNN.png" />

* This means a point close to a cluster of points classified as ‘Red’ has a higher probability of getting classified as ‘Red’.

Algo:

1. Select the K.
2. Calculate the Euclidean distance of n number of neighbours from unclassified sample.
3. Take the K nearest neighbors as per the calculated Euclidean distance.
4. Count the number of the data points in each category (as an example, K = 5, and 3 red datapoints and 2 green datapoints are closer to unclassified sample then that sample will belong to red class).
5. Assign the new data points to that category for which the number of the neighbor is maximum.

* You can read more about it in details on provided links: [Click here](https://www.geeksforgeeks.org/k-nearest-neighbours/) | [Or here](https://www.javatpoint.com/k-nearest-neighbor-algorithm-for-machine-learning) | [Or here](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)

---

### If you like my work, you can contribute to https://www.patreon.com/xscotophilic

### Thank You!