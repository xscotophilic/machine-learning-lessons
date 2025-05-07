# Classification

> Classification models are used to predict categorical class labels. They are essential in machine learning for tasks where the output is a discrete category rather than a continuous value.

## Table of Contents

- [Overview](#overview)
- [Key Terminologies](#key-terminologies)
- [Types of Classification](#types-of-classification)
- [Further Reading](#further-reading)

## Overview

Classification analysis is a statistical method used to assign items into predefined classes or categories. It is widely used for:

- Predicting discrete/categorical values (e.g., spam detection, disease diagnosis)
- Identifying patterns and groupings in data
- Quantifying the likelihood of class membership

**Use Cases:**

- Feature selection (measuring feature importance)
- Fraud detection
- Predicting customer churn

## Key Terminologies

1. **Dependent Variable**: The main factor in classification analysis that we wish to predict or understand. Also known as the target or class label.
2. **Independent Variable**: A predictor that affects the dependent variable or is used to predict its class.
3. **Confusion Matrix**: A table used to evaluate the performance of a classification model by comparing actual and predicted classes.

**Mathematical Intuition:**
- At its core, classification is about finding a function that maps input features (independent variables) to discrete output labels (dependent variable). The goal is to learn a decision boundary that best separates the classes in the feature space.
- **Decision Boundary:** This is a surface (line in 2D, plane in 3D, or hyperplane in higher dimensions) that divides the feature space into regions, each corresponding to a class label.
- **Probability Estimation:** Many classifiers (like logistic regression or Naive Bayes) estimate the probability that a sample belongs to each class, assigning the label with the highest probability.

## Types of Classification

1. **Logistic Regression**
2. **K-Nearest Neighbors (KNN)**
3. **Support Vector Machine (SVM)**
4. **Kernel SVM**
5. **Naive Bayes**
6. **Decision Tree Classification**
7. **Random Forest Classification**

Each type of classification has its own strengths and is suited for different kinds of data and problem statements.

## Further Reading

- [Classification (Wikipedia)](https://en.wikipedia.org/wiki/Statistical_classification)
- [Scikit-learn Classification Documentation](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
