# Random Forest Regression

- As the name suggests, this algorithm creates the forest with a number of Decision trees.

- Ensemble Learning

  - An ensemble approach is a strategy for making more accurate predictions by combining forecasts from various machine learning algorithms.

  - Types of Ensemble Learning:

  1. Boosting: Boosting is a set of algorithms that use weighted averages to turn weak students become good students. Each model that runs determines which features will be prioritised in the next model.

  2. Bootstrap Aggregation (Bagging): Random sampling with replacement is referred to as bootstrap. With Bootstrap, we can better grasp the dataset's bias and variance. Bagging allows each model to run separately before aggregating the results at the end without giving any model a priority.

- In general, the more trees in the forest the more robust the forest looks like. In the same way in the random forest regressor, the higher the number of trees in the forest gives the high the accuracy results.

<p align="center">
  <img src="https://user-images.githubusercontent.com/47301282/120513082-86b90200-c3e9-11eb-997f-1bfaa11e6660.png" />
</p>

- Each tree is created from a different sample of rows and at each node, a different sample of features is selected for splitting.

- Each of the trees makes its own individual prediction.

- These predictions are then averaged to produce a single result.

- The averaging makes a Random Forest better than a single Decision Tree hence improves its accuracy and reduces overfitting.

- You can read about `Random Forest Regression` in details on provided links:

  - [Random Forest Regression on medium.com](https://medium.com/swlh/random-forest-and-its-implementation-71824ced454f)
