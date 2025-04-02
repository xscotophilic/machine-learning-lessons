# Decision Tree Regression

## Decision Tree Regression is used when we are trying to predict an output variable that is continuous.

- Let’s look at a very simple decision tree. Below is a workflow that can be used to make a decision on whether or not to eat a peanut butter cookie.

<p align="center">
    <img src="https://user-images.githubusercontent.com/47301282/120511899-781e1b00-c3e8-11eb-866a-2ca6ab9cda8c.jpeg" />
</p>

- A decision tree can detect the fact that you should only eat the cookie if specific criteria are met in this case. A decision tree's ultimate purpose is to achieve this. We want to keep making decisions (splits) until we meet certain requirements. We can utilise it to classify or predict once we've encountered it.

- This is a very simple example with only two variables ( allergy, ruining dinner). However, how do you pick which variables/columns to split on if you have a dataset with thousands of variables/columns? Entropy and information gain are a popular technique to overcome this problem, especially when utilising an ID3 algorithm.

<p align="justify">
There are three sorts of nodes in this tree-structured classifier. The Root Node is the first node in the graph, and it represents the complete sample. It can be further divided into nodes. The features of a data collection are represented by the interior nodes, while the decision rules are represented by the branches. Finally, the outcome is represented by the Leaf Nodes.
</p>

<p align="center">
    <img src="https://user-images.githubusercontent.com/47301282/120511999-8ec47200-c3e8-11eb-9a7a-7775ce3c2972.png" />
</p>

- In a regression tree, a regression model is fit to the target variable using each of the independent variables. The data is then split at several points for each independent variable.

- At those points, the error between the predicted values and actual values is squared to get “A Sum of Squared Errors”(SSE). The point that has lowest SSE is chosen as the split point. This process is continued recursively.

- Some of the other methods: We may readily state that data is segmented, but have we ever considered how and why this occurs? The solution to this question can be found in two key concepts: information entropy (E) and information gain (I) (IG).

- You can read about `Decision Tree Regression` in details on provided links:

  - [Machine Learning: Decision Tree Regression on medium.com](https://medium.com/analytics-vidhya/machine-learning-decision-tree-regression-ff8563ffaf52)

  - [Entropy and Information Gain on TDS](https://towardsdatascience.com/entropy-and-information-gain-b738ca8abd2a)

  - [Entropy and Information Gain in Decision Trees on TDS](https://towardsdatascience.com/entropy-and-information-gain-in-decision-trees-c7db67a3a293)
